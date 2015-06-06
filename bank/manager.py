'''
Created on Jun 4, 2015

@author: cristopher
'''

from bank.client import Client, Account
from bank.persistence import Persistence

class Manager(object):

    def __init__(self):
        self._persistence = Persistence()
        self._clients = list()
        
    def createAccount(self, id, name):
        account = Account(id)
        client = Client(name, account)
        self._clients.append(client)
        return client
            
    def lookForClientByID(self, id):
        for c in self._clients:
            if c.id == id:
                return c
            else:
                return None
        
    def lookForClientByName(self, name):
        for c in self._clients:
            if c.name == name:
                return c
            else:
                return None

    def removeClient(self, name):
        c = self.lookForClientByName(name)
        self._clients.remove(c)

    def removeClient(self, id):
        c = self.lookForClientByID(id)
        self._clients.remove(c)

    def listClients(self):
        for c in self._clients:
            print c.toDict()

    def save(self):
        self._persistence.save(self._clients)

    def load(self):
        self._clients = self._persistence.load()