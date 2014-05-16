#!/usr/bin/python
 
import sys
 
Hits = 0
oldKey = None
 
# Loop around the data
# It will be in the format key\tval
# Where key is the request path name, val is the amount of hits from the mapper
#
# In this case we'll print out only the request path: "/assets/js/the-associates.js"
 
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
