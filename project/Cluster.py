#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Transaction import Transaction

class Cluster(object):
    '''
    create a new cluster with transactions
    @param transaction the transactions of a new cluster
    '''
    def __init__(self, transaction=[]):
        self.transactions = []
        if transaction:
            self.transactions.append(transaction)
    
    '''
    add a new transaction to the cluster
    @param transaction the new transaction
    '''
    def addTransaction(self, transaction):
        self.transactions.append(transaction)

    '''
    remove a transaction from cluster
    @param transaction the transaction is removed
    '''
    def removeTransaction(self, transaction):
        self.transactions.remove(transaction)

    '''
    get count of transactions in the cluster
    @param transactions in the cluster
    '''
    def getCluster(self):
        return self.transactions
    
    '''
    get height parameter of current cluster
    @return the height of cluster
    '''
    def getHeight(self):
        clusterHeight = 0;
        hashTableKeys = self.getHashTable().values()
        
        for height in hashTableKeys:
            if (height > clusterHeight):
                clusterHeight = height

        return clusterHeight;

    '''
    get width parameter of current cluster
    @return the width of cluster
    '''
    def getWidth(self):
        return len(self.getHashTable())
    
    '''
    checking for emptiness cluster
    @return the true if empty
    '''
    def clusterIsEmpty(self):
        return True if len(self.transactions) == 0 else False
    
    '''    
    get unique values from all transactions and the number of occurrences in the cluster
    @return the map with unique value and number of values in the cluster
    '''
    def getHashTable(self):
        hashTable = {}
        for transaction in self.transactions:
            for t in transaction:
                if t in hashTable:
                    hashTable[t] += 1
                else:
                    hashTable[t] = 1
            
        return hashTable
    
    '''
    get count of transactions in the cluster
    @return the number of transactions
    '''
    def getCountTransactions(self):
        return len(self.transactions)
    
    def toString(self):
        #return "{" + str(self.transactions) + "}"
        return str(self.transactions)
    
if __name__ == "__main__":    
    t1 = Transaction('a,b,a,d').getTransaction()
    t2 = Transaction('b,f,d').getTransaction()
    t3 = Transaction().getTransaction()
    
    print 'empty cluster:'
    cluster1 = Cluster()
    print cluster1.getCluster()
    
    print 'add cluster:'
    cluster2 = Cluster(t1)
    cluster2.addTransaction(t2)
    cluster2.addTransaction(t3)
    print cluster2.getCluster()
    
    print 'remove from cluster:'
    cluster2.removeTransaction(t3)
    print cluster2.getCluster()
    
    print 'hashTable:'
    print cluster2.getHashTable()
    
    print 'count transaction:'
    print cluster2.getCountTransactions()
    print 'height:'
    print cluster2.getHeight()
    print 'width:'
    print cluster2.getWidth()
    
    print 'claster is empty:'
    print cluster2.clusterIsEmpty()
    
    print 'claster is empty:'
    print cluster1.clusterIsEmpty()
    
    print cluster2.toString()
    
    