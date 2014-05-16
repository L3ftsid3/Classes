#!/usr/bin/python
 
import sys
 
Hits = 0
oldKey = None
 
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
 
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
 
    thisKey, thisHits = data_mapped
    thisHits = int(thisHits)
     
    if oldKey == None:
        oldKey = thisKey
 
    if oldKey != thisKey:
        if oldKey == "/assets/js/the-associates.js"
            print oldKey, "\t", Hits
        oldKey = thisKey;
        Hits = 0
 
    Hits += thisHits
 
if oldKey != None:
    if oldKey == "/assets/js/the-associates.js"
        print oldKey, "\t", Hits
