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

value = client1.withdraw(50)

print value

print client1.toString()

client2 = manager.createAccount(2341, 'Joao da Vida')

print client2.toString()

client1.transfer((manager.lookForClientByID(2341)),50)

print client1.genReport()
print client2.genReport()

