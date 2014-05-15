!/usr/bin/python

#Excercise 1 - The three questions that you have to answer about this data set are:
# Instead of breaking the sales down by store, instead give us a sales breakdown by product category across all of our stores.
#    Find the monetary value for the highest individual sale for each separate store.
#    Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.


# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 4 (item) and 5 (cost) [KEY = item descr., VALUE = cost]
# We need to write them out to std output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print"{0}\t{1}".format(item, cost)
