#!/usr/bin/python
#Cisco Endpoint Management Toolkit
#Author: Jason Keyes
#Description: Toolkit to easily manage Cisco Telepresence Endpoints from the command lineself.


import sys
Modules = sys.path.append('/Modules')

prompt = "> "

class Engine(object):
    #The engine which runs the toolkit
    def __init__(self, name):
        self.name = name
    def run (self):
        welcome = Menu('initial', 'Welcome to CEMT!\nplease select your option below:\n\n', ['1) Deploy new Endpoint','2) Bulk Administration','3) Status check (online/offline)','4) Connect to Endpoint','0) Exit'])
        welcome.printMenu()
        optionSelect()

class Menu(object):
    name = ""
    header = ""
    menu_options = []
    #All of the menus of initial structure of application, this does not include those of each respective imported module"
    def __init__(self, name, header, menu_options):
        self.name = name
        self.header = header
        self.menu_options = menu_options
    def printMenu(self):
        print self.header
        l = len(self.menu_options)
        for x in range(l):
            entry = self.menu_options.pop(0)
            print entry

def optionSelect():
    userInput = raw_input(prompt)
    if userInput == '1':
        from Modules import endpointDeploy
    elif userInput == '2':
        bulk = Menu('bulkadmin','\n---------Bulk Administration---------\n', ['1) Bulk Connect','0) Exit'])
        bulk.printMenu()
        userInput = raw_input(prompt)
        if userInput == '0':
            sys.exit()
        elif userInput == '1':
            from Modules import massTPDConnect
        else:
            raise ValueError('Illegal Value')
    elif userInput == '3':
        from Modules import deviceAlive
    elif userInput == '4':
        from Modules import quickConnectTPD
    elif userInput == '0':
        sys.exit()
    else:
        raise ValueError('Illegal Value')

toolkit = Engine('program')
toolkit.run()
