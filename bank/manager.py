'''
Created on Jun 4, 2015

@author: cristopher
'''
from bank.client import Client, Account, Transaction

class Manager(object):

    def __init__(self):
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
        
    def lookForClientByName(self, name):
        for c in self._clients:
            if c.name == name:
                return c

    def verifyAccount(self, id):
        '''
        #TODO: Verifying if account exists or whatever.
        '''