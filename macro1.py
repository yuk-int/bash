#! /usr/bin/python
# macro1: folder for logs
# date:2024/7/27 

import os

current_path = os.path.abspath(__name__)
root_directory = os.path.dirname(current_path)
log_path = os.path.join(root_directory, 'log')
print (log_path)

if not os.path.isdir(log_path):
    print ("no path for log files, log folder is being created")
    os.mkdir(log_path)
else:
    print ('log folder is there!')

#check if 'iot.log' file in log folder (how to do it with any log?)
logs = os.path.join(root_directory, 'iot.log')
if not os.path.isfile(logs):
    print ('no log')
else:
    print ('iot.log is created')
