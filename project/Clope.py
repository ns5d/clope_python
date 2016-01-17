#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Transaction import Transaction
from Cluster import Cluster

class Clope(object):
    
    def __init__(self):
        self.clusters = []
    
    '''
    to execute the CLOPE for transactions and repulsion
    @param transactions the transactions
    @param repulsion the repulsion parameter
    @return object Clope
    '''
    def calcClope(self, filename, repulsion):            
        with open(filename, "r") as ins:
            for idx, line in enumerate(ins):
                # if (idx > 0 and idx % 50 == 0):
                #     print idx
                # print '.',
                
                transaction = Transaction(line)
                newCluster = Cluster(transaction.getTransaction())
                self.clusters.append(newCluster)
                
                profitFromNewCluster = self.getProfit(self.clusters, repulsion);
                profitMax = profitFromNewCluster;
                self.clusters.remove(newCluster);
                
                moved = False
                for cluster in self.clusters:
                    cluster.addTransaction(transaction.getTransaction())
                    profit = self.getProfit(self.clusters, repulsion)
                    
                    if (profitMax <= profit):
                        profitMax = profit
                    else:
                        cluster.removeTransaction(transaction.getTransaction());
                
                if (profitMax == profitFromNewCluster):
                    self.clusters.append(newCluster)
                    moved = True
                
                if not moved:
                    break
            #print
        return self
        
    # get profit for current distributed transactions across clusters
    def getProfit(self, clusters, repulsion):
        profit1 = 0;
        profit2 = 0;
        
        for cluster in clusters:
            #print cluster.getHashTable()
            profit1 += cluster.getHeight() * cluster.getWidth() / float(pow(cluster.getWidth(), repulsion)) * cluster.getCountTransactions()
            profit2 += cluster.getCountTransactions()
        
        return 0 if profit2 == 0 else float(profit1 / profit2)

    def toString(self):
        i = 0;
        s = ''
        for cluster in self.clusters:
            s += '\t' + str(i) + ' => ' + cluster.toString() + ',\n'
            i += 1;         
        
        return '{\n%s}' % s
    
if __name__ == "__main__":
    t1 = Transaction('a,b').getTransaction()
    t2 = Transaction('a,b,c').getTransaction()    
    cluster1 = Cluster(t1)
    cluster1.addTransaction(t2)
    print 'cluster1:'
    print cluster1.getCluster()    
    
    t3 = Transaction('e,f').getTransaction() 
    t4 = Transaction('e,g,f').getTransaction() 
    cluster2 = Cluster(t3)
    cluster2.addTransaction(t4)
    print 'cluster2:'
    print cluster2.getCluster()
    
    print "clusters:"
    clope = Clope()
    
    clusters = []
    clusters.append(cluster1)
    clusters.append(cluster2)
    print clusters
    
    print 'getProfit:'
    print clope.getProfit(clusters, 1)
    #----------------------------
    print '-' * 20
    
    filename = os.path.dirname(os.path.abspath(__file__))
    #filename = os.sep.join([filename, 'data', 'test.txt'])
    filename = os.sep.join([filename, 'data', 'agaricus-lepiota.data'])
    
    clope = Clope()
    print 'calcClope:'
    result = clope.calcClope(filename, 2.5)
    print result.toString()
 
    
    
    
    