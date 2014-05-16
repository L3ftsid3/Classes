#!/usr/bin/python

# Excercise 1 - The three questions that you have to answer about this data set are:
# Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.


# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 3 (store name) and 5 (cost) [KEY = store name, VALUE = cost]
# We need to write them out to std output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print"{0}\t{1}".format(store, cost)
