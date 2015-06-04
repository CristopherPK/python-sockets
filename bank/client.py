'''
Created on May 28, 2015

@author: cristopher
'''
from bank.clientmanager import ClientManager

class Client(object):

    def __init__(self, name, account):
        self._name = name
        self._account = account
        self._manager = ClientManager(self._account)
        
    @property
    def name(self):
        return self._name
    
    @property        
    def balance(self):
        return self._manager.balance
    
    def withdraw(self, value):
        return self._manager.take(value)
    
    def deposit(self, id = None, value):
        self._manager.put(value)
    
    def transfer(self, dst, value):
        self._manager.transfer(dst, value)
            
    def report(self):
        return self._manager.genReport()       
        