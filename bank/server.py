'''
Created on Jun 3, 2015

    Simple socket server using threads

@author: cristopher
'''

import socket
import sys
from thread import *
from bank.manager import Manager

HOST = 'localhost'
PORT = 3500
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created.'

manager = Manager()
print 'Bank connected.'

 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'

#Function for handling connections. This will be used to create threads
def clientThread(conn):
    #Sending message to connected client
    conn.send('Welcome to the bank server. Type your account ID\n') #send only takes string

    #Receiving from client
    data = conn.recv(1024)

    #Getting client by ID
    client = manager.lookForClientByID(data)
    #TODO: If the ID is invalid?
    info = client.toDict()

    #Responding the connection
    conn.send('Welcome' + info)
    #infinite loop so that function do not terminate and thread do not end.
    while True:
        #Listen to the operations from the user

        #Receiving from client
        data = conn.recv(1024)

        if not data:
            break

        elif 'PUT' == data[0:3]:
            id = data[4:8]
            value = data[9:]
            if client.id == id:
                client.deposit(value)
            else:
                client.transfer(manager.lookForClientByID(id), value)

        elif 'TAKE' in data[0:4]:
            value = data[5:]
            v = client.withdraw(value)
            conn.send(v)

        else:
            #TODO: Define invalid operations protocols.
            conn.send('Invalid operation')

    #came out of loop
    conn.close()
 
def server():
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