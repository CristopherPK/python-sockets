'''
Created on Jun 4, 2015

@author: cristopher
'''
from bank.client import Transaction, Account
from datetime import datetime

from bank.manager import Manager

manager = Manager()

client1 = manager.createAccount(1234, 'Jose Maria', 'senha')

print client1

client1.deposit(100)

print client1

value = client1.withdraw(50)

print value

print client1

client2 = manager.createAccount(2341, 'Joao da Vida', 'teste')

print client2

client1.transfer((manager.lookForClientByID(2341)),50)

print client1.genReport()
print client2.genReport()

manager.save()