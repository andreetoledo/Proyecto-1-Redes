#Andree Toledo 18439
#PROYECTO 1 REDES 2021

import os
import time
import logging
import sleekxmpp

from getpass import getpass
from prettytable import PrettyTable
from sleekxmpp.exceptions import IqError, IqTimeout

import client
from consts import *

close_login = False

# With tkinter, opens a windows for the user to select a file.
def get_file_path():
    file_path = filedialog.askopenfilename()
    return file_path

# Prints a table with all of the groups the user is part of
def print_groups(group_dict):
    table = PrettyTable()
    table.field_names = [f'{BOLD}No.{ENDC}',
                         f'{BOLD}ROOM{ENDC}',
                         f'{BOLD}NICK{ENDC}']

    table.align = 'l'
    counter = 1
    for url, group in group_dict.items():
        group_info = group.get_data()
        table.add_row([counter, group_info[0], group_info[1]])
        counter += 1

    print(table)

# Prints a table with every user and its index
def print_contact_index(user_dict):
    table = PrettyTable()
    table.field_names = [f'{BOLD}No. {ENDC}',
                         f'{BOLD}USERNAME{ENDC}',
                         f'{BOLD}SHOW{ENDC}',
                         f'{BOLD}JID{ENDC}']
    table.align = 'l'
    counter = 1
    for jid, user in user_dict.items():
        user_info = user.get_connection_data()
        table.add_row([counter, user_info[0], user_info[1], jid])
        counter += 1

    print(table)



# Prints all users through a table
def print_all_users(user_dict):
    table = PrettyTable()
    table.field_names = [f'{BOLD}USERNAME{ENDC}',
                         f'{BOLD}NAME{ENDC}',
                         f'{BOLD}EMAIL{ENDC}',
                         f'{BOLD}JID{ENDC}']
    table.align = 'l'
    for jid, user_info in user_dict.items():
        table.add_row([user_info[0], user_info[1], user_info[2], jid])

    print(table)


