'''
Created on May 28, 2015

@author: cristopher
'''
from datetime import datetime
from OpenSSL import rand

class BankAccount(object):
    
    def __init__(self, id, password):
        self._id = id
        self._password = password

    def connectBank(self):
        return str(self._id) + ' ' + str(self._password) + '\r\n'

    def balance(self):
        return 'CHECK\r\n'

    def withdraw(self, value):
        return 'TAKE ' + str(value) + '\r\n'

    def deposit(self, value):
        return 'PUT ' + str(self._id) + ' ' + str(value) + '\r\n'

    def transfer(self, dst, value):
        return 'PUT ' +  str(dst) + ' ' + str(value) + '\r\n'

class User(object):
    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._bank_account = None

    @property
    def name(self):
        return self._name        
        
    @property
    def id(self):
        return self._account.id

    @property
    def password(self):
        return self._password

    @property
    def bank(self):
        return self._bank_account

    def toDict(self):
        return {'name': self.name,
                'id': self.id}

    def addBank(self, id, password):
        self._bank_account = BankAccount(id, password)
        return 0

    def __getstate__(self): return self.__dict__

    def __setstate__(self, d): self.__dict__.update(d)