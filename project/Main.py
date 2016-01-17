#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from Clope import Clope

def main():
    if len(sys.argv) != 3:
        print 'run as:'
        print 'python ' + os.path.basename(sys.argv[0]) + ' <filename> <repulsion>'
        print 'python ' + os.path.basename(sys.argv[0]) + ' ./data/test.txt 2.5'
	print 'python ' + os.path.basename(sys.argv[0]) + ' ./data/agaricus-lepiota.data 5'

        exit(-1)
    
    filename = sys.argv[1]
    repulsion = float(sys.argv[2])
    
    if not os.path.isfile(filename):
        print "file '%s' not exists!" % filename
        exit(-2)
        
    if not isinstance(repulsion, float):
        print "repulsion must be type float [0.5, 3.2, 5,..]"
        exit(-3)
    
    # show CLOPE result
    clope = Clope()
    result = clope.calcClope(filename, repulsion)
    print result.toString()

if __name__ == "__main__":
    main()
