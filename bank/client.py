'''
Created on May 28, 2015

@author: cristopher
'''

class Transaction(object):
    
    def __init__(self, value, src, dst, op):
        self._value = value
        self._src = src
        self._dst = dst
        self._op = op

class Account(object):
    
    def __init__(self, id):
        self._id = id
        self._balance = 0 
        self._transactions = list()
    
    @property
    def id(self):
        return self._id
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, v):
        self._balance = v
    
    @property    
    def transactions(self):
        return self._transactions
    
    def newTransaction(self, transaction):
        self._transactions.append(transaction)

class Client(object):

    def __init__(self, name, account):
        self._name = name
        self._account = account
        
    @property
    def name(self):
        return self._name        
        
    @property
    def id(self):
        return self._account.id
    
    @property            
    def balance(self):
        return self._account.balance
    
    def toString(self):
        return {'name': self.name,
                'balance': self.balance,
                'id': self.id}
        
    def withdraw(self, value):
        self._account.balance(self.balance - value)
        t = Transaction(value, self._account.id, None, "withdraw")
        self._account.newTransaction(t)
        return value
        
    def deposit(self, value):
        self._account.balance(self.balance + value)
        t = Transaction(value, None, self._account.id, "deposit")
        self._account.newTransaction(t)
        
    def transfer(self, dst, value):
        v = self.withdraw(value)
        dst.deposit(self._account.id, v)
        
    def genReport(self):
        '''
        Generating reports from all your transactions on your account.
        '''
        