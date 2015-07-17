'''
Created on Jun 4, 2015

@author: cristopher
'''
from client import Client, Account
from persistence import Persistence

class Manager(object):

    def __init__(self):
        self._persistence = Persistence()
        self._clients = list()
        self._isConnected = False

    def auth(self):
        if self._isConnected is True:
            print 'FOP 100 - OK'
            return 1
        else:
            print 'FOP 200 - Unauthorized'
            return 0

    def createAccount(self, id, name, password):
        if self.auth():
            account = Account(id)
            client = Client(name, account, password)
            self._clients.append(client)
            return client

    def connectAccount(self, id, password):
        for c in self._clients:
            if c.id == id:
                if c.password == password:
                    self._isConnected = True
                    print 'FOP 100 - OK'
                    return c
                else:
                    print 'FOP 200 - Unauthorized'
                    return None
            
    def lookForClientByID(self, id):
        if self.auth():
            for c in self._clients:
                if c.id == id:
                    print 'FOP 100 - OK'
                    return c
            return None


    def lookForClientByName(self, name):
        if self.auth():
            for c in self._clients:
                if c.name == name:
                    print 'FOP 100 - OK'
                    return c
            return None


    def removeClient(self, name):
        if self.auth():
            c = self.lookForClientByName(name)
            self._clients.remove(c)

    def removeClient(self, id):
        if self.auth():
            c = self.lookForClientByID(id)
            self._clients.remove(c)

    def listClients(self):
        if self.auth():
            for c in self._clients:
                print c.toDict()

    def genReport(self):
        if self.auth():
            reports = list()
            for c in self._clients:
                reports.append(c.genReport())
            return reports

    def save(self):
        self._persistence.save(self._clients)

    def refresh(self):
        self._persistence = Persistence()
        self.load()

    def load(self):
        try:
            self._clients = self._persistence.load()
        except:
            print 'No clients existing.'
            print 'Please define a starting account.'
            id = int(raw_input("Please enter an ID: "))
            name = str(raw_input("Please enter a name: "))
            password = str(raw_input("Please enter a password: "))
            account = Account(id)
            client = Client(name, account, password)
            self._clients.append(client)
            self.save()
            print "Account created."
