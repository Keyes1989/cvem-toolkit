#!/usr/bin/python
import os
import csv
import sys
import webbrowser

filePointer = "../Resources/All_VC_Systems.csv"
script_dir = os.path.dirname(__file__) #Script Directory
endpointListFile = os.path.join(script_dir, filePointer)
prompt = "> "
print """
 _________________   _____                             _
|_   _| ___ \  _  \ /  __ \                           | |
  | | | |_/ / | | | | /  \/ ___  _ __  _ __   ___  ___| |_
  | | |  __/| | | | | |    / _ \| '_ \| '_ \ / _ \/ __| __|
  | | | |   | |/ /  | \__/\ (_) | | | | | | |  __/ (__| |_
  \_/ \_|   |___/    \____/\___/|_| |_|_| |_|\___|\___|\__|


 """
#get name of desired device
hostname = raw_input("What endpoint do you want to connect to?\n" + prompt)

#dump csv file of devices/IPs to dictionary
with open(endpointListFile, 'rb') as f:
    reader = csv.reader(open(endpointListFile))
    device_dict = {}
    for row in reader:
        device_dict[row[0]]=row[1]

def browserLauncher(endpointIP):
    new = 2
    tabURL = endpointIP
    webbrowser.open(tabURL,new=new)
    sys.exit()

#Search dictionary for input hostname
def deviceLookup(hostname, device_dict):
    if hostname in device_dict:
        endpointIP = device_dict[hostname]
        #automatically launch browser to corresponding IP address/hostname of searched device
        browserLauncher("https://"+endpointIP+"/web/signin")
    else:
        raise ValueError('Device Not Found')

deviceLookup(hostname, device_dict)
