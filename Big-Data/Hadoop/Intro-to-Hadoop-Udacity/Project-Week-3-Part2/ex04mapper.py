#!/usr/bin/python
 
# Format of each line is:
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
# %h %l %u %t \"%r\" %>s %b
# IP client_ID client_username time request status_code object_size
#
# We need hits to a certain path. 
# The request path is extracted from the request. Since we need hits the value will be 1 [KEY: request_path , VALUE: 1]
# We need to write them out to standard output, separated by a tab
 
 
# To better split a log
#p = re.compile(
#    '([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
#    )

#for line in file.readlines():
#    m = p.match(line)
#    if not m:
#        continue
#    host, ignore, user, date, request, status, size = m.groups()


import sys
req_path_array = []
 
for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
    # time and zone will have a square bracket to remove with regex (in this mapper it's not needed)
        IP, client_ID, client_username, time, zone, req_method, req_path, protocol, status_code, object_size = data
        # request_path = request.split(" ")[1]
        # print "Path" + str(req_path)
        req_path_array.append(req_path)
         
# Optimize mapper phase by doing a small reduce phase within the same mapper (saves time on shuffling phase)
def add_values_within_mapper(key_array):
    dict = {}
    for element in range(len(key_array)):
        if not(key_array[element] in dict):
            dict[key_array[element]] = 1
        else:
            dict[key_array[element]] += 1
    return dict
 
def print_map_phase(dict):
    for key, value in dict.items():
        print"{0}\t{1}".format(key, value)
 
added_values = add_values_within_mapper(req_path_array)
print_map_phase(added_values)
