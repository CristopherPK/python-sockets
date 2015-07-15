'''
Created on Jun 3, 2015

    Simple socket server using threads

@author: cristopher
'''

# Echo client program
from ibus.keysyms import key
import socket
from wallet.manager import Manager

HOST = 'localhost'     # The remote host
PORT = 8888            # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
manager = Manager()

def start():
    s.connect((HOST, PORT))
    #Receiving the first message from server.
    s.recv(1024)

    try:
        manager.load()
    except:
        pass

    if manager.user is None:
        username = input('Insert your username: ')
        password = input('Insert your password: ')
        manager.createUser(username, password)
        id = input('Insert your bank id: ')
        bank_pass = input('Insert your bank password: ')
        manager.user.addBank(int(id), str(bank_pass))

    bank = manager.user.bank
    s.send(bank.connectBank())
    s.recv(1024)

    while True:
        print "------------------\n" \
        "1 - Check balance\n" \
        "2 - Deposit\n" \
        "3 - Withdraw\n" \
        "4 - Transfer\n" \
        "0 - Exit\n" \
        "------------------\n"

        x = int(input("Please enter an option: "))

        if x == 1:
            balance(bank)
        elif x == 2:
            value = input('Insert the value: ')
            deposit(bank, int(value))
        elif x == 3:
            value = input('Insert the value: ')
            withdraw(bank, int(value))
        elif x == 4:
            dst = input('Insert the destination account id: ')
            value = input('Insert the value: ')
            transfer(bank, dst, value)
        elif x == 0:
            exit()
            print 'Finishing...'
            break
        else:
            print 'Invalid operation'
            continue

    manager.save()

def balance(bank):
    s.send(bank.balance())
    print s.recv(1024)

def withdraw(bank, value):
    s.send(bank.withdraw(value))
    print s.recv(1024)

def deposit(bank, value):
    s.send(bank.deposit(value))
    print s.recv(1024)

def transfer(bank, dst, value):
    s.send(bank.transfer(dst, value))
    print s.recv(1024)

def exit():
    s.send('.')
    s.close()

if __name__ == '__main__':
    start()