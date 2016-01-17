#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Transaction(object):
    sep = ","
    
    # create a new transaction
    def __init__(self, transaction = ''):
        self.transaction = []        
        if transaction:
            self.transaction = transaction.strip().split(self.sep)        
    
    # get transaction
    def getTransaction(self):
        return self.transaction
    
    def toString(self):
        return self.sep.join(self.transaction)
    

if __name__ == "__main__":
    #t = Transaction()
    t = Transaction('a,b,c')
    print t.getTransaction()
    print t.toString()
