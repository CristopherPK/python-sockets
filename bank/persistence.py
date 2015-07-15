'''
Created on Jun 4, 2015

@author: cristopher
'''

import pickle as pkl

datapath = ".data/"

class Persistence(object):

    def __init__(self):
        self._output = []

    def save(self, obj):
        self._output = open(datapath + 'data.pkl', 'wa')
        self._pickler = pkl.Pickler(self._output)
        self._pickler.dump(obj)
        self._output.close()
        print 'Dumping object'

    def load(self):
        self._output = open(datapath + 'data.pkl', 'rb')
        self._unpickler = pkl.Unpickler(self._output)
        return self._unpickler.load()

