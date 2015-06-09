'''
Created on Jun 4, 2015

@author: cristopher
'''
from bank.client import Client, Account
from bank.persistence import Persistence

class Manager(object):

    def __init__(self):
        self._persistence = Persistence()
        self._clients = list()
        
    def createAccount(self, id, name):
        account = Account(id)
        client = Client(name, account)
        self._clients.append(client)
        return client
            
    def lookForClientByID(self, id):
        for c in self._clients:
            if c.id == id:
                return c
        
    def lookForClientByName(self, name):
        for c in self._clients:
            if c.name == name:
                return c

    def removeClient(self, name):
        c = self.lookForClientByName(name)
        self._clients.remove(c)

    def removeClient(self, id):
        c = self.lookForClientByID(id)
        self._clients.remove(c)

    def listClients(self):
        for c in self._clients:
            print c.toDict()

    def genReport(self):
        #TODO: Implement the reports.
        print "ok"

    def save(self):
        self._persistence.save(self._clients)

    def load(self):
        self._clients = self._persistence.load()

    def ui(self):

        while True:
            print "------------------\n" \
            "1 - Add Client\n" \
            "2 - List Clients\n" \
            "3 - Remove Client\n" \
            "4 - Reports\n" \
            "0 - Exit\n" \
            "------------------\n"

            x = int(input("Please enter an option: "))

            if x == 1:
                id = int(raw_input("Please enter an ID: "))
                name = str(raw_input("Please enter a name: "))
                c = self.createAccount(id, name)
                print "Account created."
                self.save()
            elif x == 2:
                self.listClients()
            elif x == 3:
                id = int(raw_input("Please enter an ID: "))
                self.removeClient(id)
                self.save()
            elif x == 4:
                self.genReport()
            else:
                break

if __name__ == '__main__':
    m = Manager()
    m.load()
    m.ui()