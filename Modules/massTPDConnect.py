#!/usr/bin/python
import time, csv
from pexpect import pxssh
from sys import argv
import os

#csv file must just be list of IP addresses, as only rotates through first column
filePointer = "../Resources/bulk_endpoints.csv"
script_dir = os.path.dirname(__file__) #Script Directory
endpointListFile = os.path.join(script_dir, filePointer)

print"""\n

 _____          _             _       _    ______       _ _     ______ _       _
|  ___|        | |           (_)     | |   | ___ \     | | |    |  _  (_)     | |
| |__ _ __   __| |_ __   ___  _ _ __ | |_  | |_/ /_   _| | | __ | | | |_  __ _| | ___ _ __
|  __| '_ \ / _` | '_ \ / _ \| | '_ \| __| | ___ \ | | | | |/ / | | | | |/ _` | |/ _ \ '__|
| |__| | | | (_| | |_) | (_) | | | | | |_  | |_/ / |_| | |   <  | |/ /| | (_| | |  __/ |
\____/_| |_|\__,_| .__/ \___/|_|_| |_|\__| \____/ \__,_|_|_|\_\ |___/ |_|\__,_|_|\___|_|
                 | |
                 |_|

\n\n"""

#hostname = raw_input("\nWhat endpoint to connect to? ")
username = raw_input("\nUsername: ")
secretPW = raw_input("\nPassword: ")
sipNumber = raw_input("\nNumber to Dial: ")
reader = csv.reader(open(csvFile))

def disconnectTPD(s):
    s.prompt()
    s.sendline('bye')

def connectTPD(s, endpointIP, username, secretPW):
    s.force_password = True
    s.PROMPT = 'SSH>'
    s.login(endpointIP, username, secretPW, auto_prompt_reset = False)
    s.prompt()
    #print "\nConnection to device established\n"

for row in reader:
    deviceIP = row[0]
    s = pxssh.pxssh(timeout=1, maxread=2000000)
    connectTPD(s, deviceIP, username, secretPW)
    uCMD = "xCommand Dial Number: %s Protocol: SIP" %s
    time.sleep(1)
    s.sendline(uCMD)
    time.sleep(2)
    data = s.before
    print data
    disconnectTPD(s)
