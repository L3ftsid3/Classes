#!/usr/bin/python

import sys

maxSale = 0
oldKey = None

# Loop around the data
# It will be in format key\tvalue
# Where key is the store name, val is the sale amount
#
# All the sales for a particular item will be presented, 
# then the key will change and we'll be dealing with the next item

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip the line
        continue
    
    thisKey, thisSale = data_mapped
    
    # When key has just been changed (From Miami to NYC stores)
    if oldKey and oldKey != thisKey:
        # print result from oldKey (previous store)
        print oldKey, "\t", salesTotal
        # Change the key to the new store
        oldKey = thisKey
        #Reset maxSale value for the new store to compute new max
        maxSale = 0
        
    if oldKey == None:
        oldKey = thisKey
        
    if thisSale > maxSale:
        maxSale = thisSale
    
if oldKey != None:
    print oldKey, "\t", maxSale
    













