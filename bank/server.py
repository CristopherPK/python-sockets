'''
Created on Jun 3, 2015

    Simple socket server using threads

@author: cristopher
'''

import socket
import sys
from thread import *
from manager import Manager

HOST = 'localhost'
PORT = input('Insert your server address port: ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created.'


#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

def refresh(id, password):
    manager = Manager()
    manager.load()
    manager.connectAccount(id,password)
    return manager

#Function for handling connections. This will be used to create threads
def clientThread(conn):
    #Sending message to connected client
    conn.send('Welcome to the bank server. Type your account ID and your password\n') #send only takes string

    manager = Manager()
    #manager.listClients()

    #infinite loop so that function do not terminate and thread do not end.
    while True:
        manager.load()

        #Listen to the operations from the user
        #Receiving from client
        data = conn.recv(1024)

        print repr(data)

        if not data or data[0] is '.':
            print 'Closing connection'
            conn.send('Quiting...\n')
            client = None
            break

        id = int(data[:4])
        #print id
        password = str(data[5:len(data)-1])
        #print password
        #print len(password)
        password = password[:len(password)-1]

        #Getting client by ID
        client = manager.connectAccount(id,password)
        print 'Bank connected.'

        print client

        if client is None:
            conn.send('ID invalid.\n')
            continue
        else:
            info = client.toDict()
            #Responding the connection
            conn.send('OK')
            break

    #Infinite loop to capture client operations.
    while True:
        if client is None:
            print 'Closing connection'
            conn.send('Quiting...\n')
            break

        data = conn.recv(1024)

        manager.refresh()
        client = manager.connectAccount(id, password)


        if 'PUT ' == data[0:4]:
            dst_id = int(data[4:8])
            value = int(data[9:])
            if client.id == dst_id:
                data = client.deposit(value)
                manager.save()
                conn.send(data  + '\n')
            else:
                data = client.transfer(manager.lookForClientByID(dst_id), value)
                manager.save()
                conn.send(data + '\n')


        elif 'TAKE ' in data[0:5]:
            value = int(data[5:])
            v = client.withdraw(value)
            manager.save()
            conn.send(str(v) + '\n')

        elif 'CHECK' in data:
            conn.send(str(client.balance) + '\n')

        elif data[0] == '.':
            conn.send('Quiting... \n')
            break

        else:
            print 'FOP 300 - Invalid Operation'
            conn.send('Invalid operation\n')
            continue

        #manager = refresh(id, password)
        #print 'Refreshing server...'

    #came out of loop
    conn.close()

#Start listening on socket
s.listen(10)
print 'Socket now listening'

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientThread ,(conn,))

s.close()