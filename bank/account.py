'''
Created on Jun 4, 2015

@author: cristopher
'''

class Account(object):
    def __init__(self):
        self.id = [] # Inicializar o id de acordo com os id's existentes
        self.balance = 0 # 
        self.transactions = list() #
    
    @property
    def id(self):
        return self.id
    
    @property
    def balance(self):
        return self.balance
    
    @balance.setter
    def balance(self, v):
        self.balance = v
    
    @property    
    def transactions(self):
        return self.transactions
    
    def newTransaction(self, transaction):
        self.transactions.add(transaction)