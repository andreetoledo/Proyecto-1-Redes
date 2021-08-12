#Andree Toledo 18439
#PROYECTO 1 REDES 2021

import os
import time
import logging
import getpass
import threading
import base64
import datetime
import mimetypes

from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout
from xml.etree import cElementTree as ET
from sleekxmpp.plugins.xep_0004.stanza.field import FormField, FieldOption
from sleekxmpp.plugins.xep_0004.stanza.form import Form
from sleekxmpp.plugins.xep_0047.stream import IBBytestream
from consts import OKGREEN, OKBLUE, WARNING, FAIL, ENDC, BLUE, RED, NEW_MESSAGE, FILE_OFFER, SUSCRIPTION, GOT_ONLINE, error_msg, GROUPCHAT, STREAM_TRANSFER


DIRNAME = os.path.dirname(__file__)


class Client(ClientXMPP):

    def __init__(self, jid, password):

        ClientXMPP.__init__(self, jid, password)
        self.auto_authorize = True
        self.auto_subscribe = True
        self.contact_dict = {}
        self.user_dict = {}
        self.room_dict = {}
        self.file_received = ''

        # self.add_event_handler('session_start', self.session_start)
        self.add_event_handler('message', self.received_message)
        self.add_event_handler('disconnected', self.got_disconnected)
        self.add_event_handler('failed_auth', self.on_failed_auth)
        self.add_event_handler('presence_subscribed',
                               self.new_presence_subscribed)
        self.add_event_handler("got_offline", self.presence_offline)
        self.add_event_handler("got_online", self.presence_online)
        self.add_event_handler('changed_status', self.wait_for_presences)
        self.add_event_handler('groupchat_presence',
                               self.on_groupchat_presence)

        # FILE TRANSFER
        self.add_event_handler('si_request', self.on_si_request)
        self.add_event_handler('ibb_stream_start', self.on_stream_start)
        self.add_event_handler("ibb_stream_data", self.stream_data)
        self.add_event_handler("ibb_stream_end", self.stream_closed)

        self.register_plugin('xep_0030')
        self.register_plugin('xep_0004')
        self.register_plugin('xep_0066')
        self.register_plugin('xep_0077')
        self.register_plugin('xep_0050')
        self.register_plugin('xep_0047')
        self.register_plugin('xep_0231')
        self.register_plugin('xep_0045')
        self.register_plugin('xep_0095')  # Offer and accept a file transfer
        self.register_plugin('xep_0096')  # Request file transfer intermediate
        self.register_plugin('xep_0047')  # Bytestreams

        self['xep_0077'].force_registration = True

        self.received = set()
        self.presences_received = threading.Event()
    
    def session_start(self):
        try:
            self.get_roster(block=True)
        except IqError as err:
            print('Error: %s' % err.iq['error']['condition'])
        except IqTimeout:
            print('Error: Request timed out')

        self.send_presence()

    # Create a new user dict
    def create_user_dict(self, wait=False):

        try:
            self.get_roster(block=True)
        except IqError as err:
            print('Error: %s' % err.iq['error']['condition'])
        except IqTimeout:
            print('Error: Request timed out')

        groups = self.client_roster.groups()
        for jid in groups['']:
            # Check we are not evaluating ourselves or a conference room
            if jid == self.boundjid.bare or 'conference' in jid:
                continue

            # Get some data
            sub = self.client_roster[jid]['subscription']
            name = self.client_roster[jid]['name']
            username = str(jid.split('@')[0])
            connections = self.client_roster.presence(jid)

            # Check if connections is empty
            if connections.items():
                # Go through each connection
                for res, pres in connections.items():

                    show = 'available'
                    status = ''
                    if pres['show']:
                        show = pres['show']
                    if pres['status']:
                        status = pres['status']

                    # Check if the user is in the dict, else add it
                    if not jid in self.contact_dict:
                        self.contact_dict[jid] = User(
                            jid, name, show, status, sub, username, res)
                    else:
                        self.contact_dict[jid].update_data(
                            status, show, res, sub)

            # User is not connected, still add him to the dict
            else:
                self.contact_dict[jid] = User(
                    jid, name, 'unavailable', '', sub, username, '')

    # Returns a dict jid - User. If it's empty, create it.
    def get_user_dict(self):
        if not self.contact_dict:
            self.create_user_dict()
        return self.contact_dict

    # Create user dict on new presence
    def wait_for_presences(self, pres):
        self.received.add(pres['from'].bare)
        if len(self.received) >= len(self.client_roster.keys()):
            self.presences_received.set()
        else:
            self.presences_received.clear()

        self.create_user_dict()

    # Act upon a received message
    def received_message(self, msg):

        sender = str(msg['from'])
        jid = sender.split('/')[0]
        username = jid.split('@')[0]
        if msg['type'] in ('chat', 'normal'):
            print(f'{BLUE}{NEW_MESSAGE} New message from {jid}{ENDC}')

            if not jid in self.contact_dict:
                self.contact_dict[jid] = User(
                    jid, '', '', '', '', username)

            self.contact_dict[jid].add_message_to_list((username, msg['body']))

        elif msg['type'] in ('groupchat', 'normal'):
            nick = sender.split('/')[1]

            # don't let you get a notification from yourself
            if jid in self.room_dict:
                self.room_dict[jid].add_message_to_list((nick, msg['body']))
                if nick != self.room_dict[jid].nick:
                    print(
                        f'{BLUE}{GROUPCHAT} New message from {nick} in {jid}{ENDC}')

    def request_si(self, user_jid, file_path):

        file_path = file_path.replace('\\', '/')
        # Get some  data from the file
        file_name = file_path.split('/')[-1]
        file_size = os.path.getsize(file_path)
        unix_date = os.path.getmtime(file_path)
        file_date = datetime.datetime.utcfromtimestamp(
            unix_date).strftime('%Y-%m-%dT%H:%M:%SZ')
        file_mime_type = 'not defined'

        try:
            file_mime_type = str(
                mimetypes.MimeTypes().guess_type(file_path)[0])
        except:
            pass

        data = None
        # Read the contents of the file and encode it to b64
        with open(file_path, 'rb') as file:
            data = base64.b64encode(file.read()).decode('utf-8')

        # Set the data of the request
        dest = self.contact_dict[user_jid].get_full_jid()

        try:

            req = self.plugin['xep_0096'].request_file_transfer(
                jid=dest,
                name=file_name,
                size=file_size,
                mime_type=file_mime_type,
                sid='ibb_file_transfer',
                desc='Envío un archivo con descripción',
                date=file_date
            )

            # Wait for the other user to accept the file transfer
            print(f'{BLUE}{FILE_OFFER} Offering a file transfer to the user.{ENDC}')
            time.sleep(2)

            # Open the ibb stream transfer
            stream = self.plugin['xep_0047'].open_stream(
                jid=dest, sid='ibb_file_transfer', ifrom=self.boundjid.full)

            # Wait for the other client to get notified about this
            time.sleep(2)
