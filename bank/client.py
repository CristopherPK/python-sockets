'''
Created on May 28, 2015

@author: cristopher
'''
from datetime import datetime
from OpenSSL import rand

class Transaction(object):
    
    def __init__(self, time, value, src, dst, op):
        self._time = time
        self._value = value
        self._src = src
        self._dst = dst
        self._op = op

    def __getstate__(self): return self.__dict__

    def __setstate__(self, d): self.__dict__.update(d)

    def toDict(self):
        return {'time': self._time,
                'value': self._value,
                'src': self._src,
                'dst': self._dst,
                'op': self._op}

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
    
    def setBalance(self, v):
        self._balance = v
    
    @property    
    def transactions(self):
        return self._transactions
    
    def newTransaction(self, transaction):
        self._transactions.append(transaction)

class Client(object):
    def __init__(self, name, account, password):
        self._name = name
        self._account = account
        self._password = password

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
    def balance(self):
        return self._account.balance
    
    def toDict(self):
        return {'name': self.name,
                'balance': self.balance,
                'id': self.id}

    def withdraw(self, value):
        if self.balance - value < 0:
            print 'FOP 101 - Funds insufficient'
            return 0
        else:
            self._account.setBalance(self.balance - value)
            t = Transaction(datetime.now().time(), value, self._account.id, None, "withdraw")
            self._account.newTransaction(t)
            print 'FOP 200 - OK'
            return value
        
    def deposit(self, value):
        self._account.setBalance(self.balance + value)
        t = Transaction(datetime.now().time(), value, None, self._account.id, "deposit")
        self._account.newTransaction(t)
        print 'FOP 200 - OK'
        return 'Done'

    def transfer(self, dst, value):
        if dst is not None:
            self._account.setBalance(self.balance - value)
            dst._account.setBalance(dst.balance + value)
            t = Transaction(datetime.now().time(), value, self._account.id, dst.id, "transfer")
            self._account.newTransaction(t)
            dst._account.newTransaction(t)
            print 'FOP 200 - OK'
            return 'Done'
        else:
            print 'FOP 201 - Account no existing'
            return 'Account no existing'


    def genReport(self):
        report = list()
        for t in self._account.transactions:
            report.append(t.toDict())
        return report

    def __getstate__(self): return self.__dict__

    def __setstate__(self, d): self.__dict__.update(d)