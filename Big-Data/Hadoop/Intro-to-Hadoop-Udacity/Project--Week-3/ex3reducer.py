#!/usr/bin/python
 
import sys
 
salesCount = 0
totalSales = 0
 
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales will be saved in the two variables:
# salesCount (number of sales)
# totalSales (total Value of the sales)
 
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
 
    thisKey, thisSale = data_mapped
 
    salesCount += 1
    totalSales += float(thisSale)
 
print salesCount, "\t", totalSales

