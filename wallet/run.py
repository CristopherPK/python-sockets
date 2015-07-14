'''
Created on Jun 3, 2015

    Simple socket server using threads

@author: cristopher
'''

# Echo client program
import socket
from wallet.manager import Manager

HOST = 'localhost'     # The remote host
PORT = 8888            # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
manager = Manager()

def start():
    s.connect((HOST, PORT))
    try:
        manager.load()
    except:
        pass

    if manager.user is None:
        manager.createUser('Freddie', '12345')
        manager.user.addBank(1234, 'senha')
        manager.save()

def balance():
    bank = manager.user.bank
    s.recv(1024)
    s.send(bank.connectBank())
    s.recv(1024)
    s.send(bank.balance())
    data = s.recv(1024)
    return data

def withdraw(value):
    s.send(bank.withdraw(value))

def deposit(value):
    s.send(bank.deposit(value))

def transfer(dst, value):
    s.send(bank.withdraw(dst, value))

def exit():
    s.send('.')
    s.close()

if __name__ == '__main__':
    start()
    print balance()
    exit()