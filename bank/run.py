'''
Created on Jun 4, 2015

@author: cristopher
'''
from bank.manager import Manager

manager = Manager()

client1 = manager.createAccount(1234, 'Jose Maria')

print client1.toString()

client1.deposit(100)

print client1.toString()