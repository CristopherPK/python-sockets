'''
Created on Jun 4, 2015

@author: cristopher
'''
from persistence import Persistence
from user import User


class Manager(object):

    def __init__(self):
        self._user = None
        self._persistence = Persistence()

    @property
    def user(self):
        return self._user

    def createUser(self, name, password):
        self._user = User(name, password)

    def save(self):
        self._persistence.save(self._user)

    def load(self):
        self._user = self._persistence.load()