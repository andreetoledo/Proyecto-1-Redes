#Andree Toledo 18439
#PROYECTO 1 REDES 2021

import os
import time

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