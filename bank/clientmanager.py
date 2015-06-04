'''
Created on Jun 4, 2015

@author: cristopher
'''
# TODO(cristopherpk): Implement transactions

class ClientManager(object):

    def __init__(self, account):
        self._account = account
        self._id = self._account.id
        self._balance = self._account.balance
        
    def updateBalance(self):
        self._account.balance(self._balance)
            
    def balance(self):
        return self._account.balance
        
    def put(self, value):
        self._balance = self.balance + value
        self.updateBalance()
        print 'Seu novo saldo é de ' + self.balance()
        
    def take(self, value):
        self._balance = self.balance - value
        self.updateBalance()  
        return value 
        
    def transfer(self, dst, value):
        v = self.take(value)
        dst.deposit(self._id, v)
        