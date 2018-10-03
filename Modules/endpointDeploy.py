#!/usr/bin/python
import os
import time
import csv
import progressbar
import subprocess
import sys
from pexpect import pxssh
from shutil import copyfile

script_dir = os.path.dirname(__file__) #Script Directory
config_file = os.path.join(script_dir, "../Resources/tpeconfig.csv")

#Banner
print """
 ___________ _____   ______           _                                  _
|_   _| ___ \  ___|  |  _  \         | |                                | |
  | | | |_/ / |__    | | | |___ _ __ | | ___  _   _ _ __ ___   ___ _ __ | |_
  | | |  __/|  __|   | | | / _ \ '_ \| |/ _ \| | | | '_ ` _ \ / _ \ '_ \| __|
  | | | |   | |___   | |/ /  __/ |_) | | (_) | |_| | | | | | |  __/ | | | |_
  \_/ \_|   \____/   |___/ \___| .__/|_|\___/ \__, |_| |_| |_|\___|_| |_|\__|
                               | |             __/ |
                               |_|            |___/

"""
reader = csv.reader(open(config_file))
commandList = []
deviceName = raw_input("What is the name of this device?\n > ")
deviceNumber = raw_input("What is the number of this device?\n > ")
newPass = raw_input("What should the new admin password for this device be?\n >")
domain = #PUT YOUR VIDEO DOMAIN HERE

class connection(object):
    deviceIP = raw_input("What is the IP address of this device?\n > ")
    username = raw_input("Username:\n >")
    secretPW = raw_input("Current Password:\n >")
    s = ""
    def __init__(self, s, deviceIP, username, secretPW):
        self.s = s
        self.epIP = deviceIP
        self.username = username
        self.secretPW = secretPW
        self.cmd = ''
    def connectTPD(self):
        self.s.force_password = True
        self.s.PROMPT = 'SSH>'
        self.s.login(self.deviceIP, self.username, self.secretPW, auto_prompt_reset = False)
        self.s.prompt()
        print "\nConnection to device established\n"
        #data = self.s.before
        #print data
    def sendCMD(self, cmd):
        time.sleep(1)
        self.s.sendline(cmd)
    def disconnectTPD(self):
        self.s.prompt()
        self.s.sendline('bye')


region = ""
dns_server_1 = ""
dns_server_2 = ""
dns_server_3 = ""
deviceIP = ""
s = pxssh.pxssh(timeout=1, maxread=2000000)
timeZone = ""
timeZone2 = ""

def deviceReachable(deviceIP):
    result = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", "-q", deviceIP]).wait()
    time.sleep(1)
    if result:
        print "No Response: " + deviceIP
        sys.exit()

#Appends user entered commands to a list and then writes to csv file
def appendUserInput(inputList, deviceNumber, deviceName, domain, newPass):
    commandList.append(("xConfiguration H323 Profile 1 H323Alias E164: %s") % deviceNumber)
    commandList.append(("xConfiguration H323 Profile 1 H323Alias ID: %s") % deviceName)
    commandList.append(("xConfiguration SIP DisplayName: %s") % deviceName)
    commandList.append(("xConfiguration SIP URI: %s"domain) % deviceNumber)
    commandList.append(("xConfiguration SystemUnit Name: %s") % deviceName)
    commandList.append("xConfiguration Time Zone: Japan") #change this for using different regions
    commandList.append("systemtools passwd")
    commandList.append("")
    commandList.append(newPass)
    commandList.append(newPass)

#unload csv to list and append additionally required commands
for row in reader:
    config = row[0]
    commandList.append(config)
appendUserInput(commandList, deviceNumber, deviceName, newPass)
entryCount = len(commandList)
c1 = connection(pxssh.pxssh(timeout=1, maxread=2000000), deviceIP, username, secretPW)
deviceReachable(c1.deviceIP)
c1.connectTPD()
time.sleep(2)
#loop through list of commands within a progress bar
with progressbar.ProgressBar(max_value=entryCount) as bar:
    for i in range(entryCount):
        command = commandList.pop(0)
        x = str(command).strip("'")
        c1.sendCMD(x)
        time.sleep(2)
        bar.update(i)
c1.disconnectTPD()
