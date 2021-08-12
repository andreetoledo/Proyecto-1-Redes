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

def get_file_path():
    file_path = filedialog.askopenfilename()
    return file_path