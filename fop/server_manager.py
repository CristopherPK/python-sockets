__author__ = 'cristopher'

class ServerManager(object):
    def __init__(self):
        '''

        :return:
        '''
    def __init__(self):
        self._persistence = Persistence()
        self._clients = list()
        self._isConnected = False

    def auth(self):
        if self._isConnected is True:
            print 'FOP 100 - OK'
            return 1
        else:
            print 'FOP 200 - Unauthorized'
            return 0


    #TODO: Who have auth to create accounts?
    def createAccount(self, id, name, password):
        account = Account(id)
        client = Client(name, account, password)
        self._clients.append(client)
        return client

    #TODO: Admin and clients shouldn't have the same functions.
    def connectAccount(self, id, password):
        #TODO: If the list is too large?
        for c in self._clients:
            if c.id == id:
                if c.password == password:
                    self._isConnected = True
                    print 'FOP 100 - OK'
                    return c
                else:
                    print 'FOP 200 - Unauthorized'
                    return None

    def lookForClientByID(self, id):
        if self.auth():
            for c in self._clients:
                if c.id == id:
                    #TODO: If the client does not exist?
                    print 'FOP 100 - OK'
                    return c


    def lookForClientByName(self, name):
        if self.auth():
            for c in self._clients:
                if c.name == name:
                    print 'FOP 100 - OK'
                    return c


    def removeClient(self, name):
        if self.auth():
            c = self.lookForClientByName(name)
            self._clients.remove(c)

    def removeClient(self, id):
        if self.auth():
            c = self.lookForClientByID(id)
            self._clients.remove(c)

    def listClients(self):
        if self.auth():
            for c in self._clients:
                print c.toDict()

    def genReport(self):
        #TODO: Implement the reports.
        print "ok"

    def save(self):
        self._persistence.save(self._clients)

    def load(self):
        self._clients = self._persistence.load()

