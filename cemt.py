#!/usr/bin/python
#Cisco Endpoint Management Toolkit
#Autho: Jason Keyes
#Description: Toolkit to easily manage Cisco Telepresence Endpoints from the command lineself.


import sys
Modules = sys.path.append('/Modules')

prompt = "> "

class Engine(object):
    #The engine which runs the toolkit
    def __init__(self, name):
        self.name = name
    def run (self):
        welcome = Menu('initial')
        welcome.initialMenu()

class Menu(object):
    #All of the menus of initial structure of application, this does not include those of each respective imported module"
    def __init__(self, name):
        self.name = name
    #launch the initial Menu"
    def initialMenu(name):
        print """Welcome to CEMT!\nplease select your option below:\n\n1) Deploy new Endpoint\n2) Bulk Administration\n3) Status check (online/offline)\n4) Connect to Endpoint\n0) Exit
        """
        possibleArgs = 5
        optionSelect()
    #Populate a new menu with fields
    def addField(self, field):
        print field
        pass
    def printMenu(self):
        print """---------Bulk Administration---------\n\n1) """



def optionSelect():
    userInput = raw_input(prompt)
    if userInput == '1':
        from Modules import jpEndpointDeploy
    elif userInput == '2':
        print "2"
        bulk = Menu('bulkAdmin')
        bulk.printMenu()
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
