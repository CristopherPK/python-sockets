'''
Created on Jun 4, 2015

@author: cristopher
'''

class Transaction(object):

    def __init__(self, value, src, dst, type):
        self._value = value
        self._src = src
        self._dst = dst
        self._type = type
        