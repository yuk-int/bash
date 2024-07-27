#! /usr/bin/python
# macro1: folder for logs
# date:2024/7/27 

import os, datetime, random

current_path = os.path.abspath(__name__)
root_directory = os.path.dirname(current_path)
log_directory = os.path.join(root_directory, 'log')
print (log_directory)

if not os.path.isdir(log_directory):
    print ("no path for log files, log folder is being created")
    os.mkdir(log_directory)
else:
    print ('log folder is there!')

#time precessing for log records
time = datetime.datetime.now()
time = time.strftime('%a %d %b %Y, %I:%M%p')

#sensor data simulation
humidity = str(random.randint(20,101)/10)

celsius = str(random.randint(0,50)/10)


#check if 'iot.log' file in log folder (how to do it with any log?)
log_iot = os.path.join(log_directory, 'iot.log')
if not os.path.isfile(log_iot):
    print ('no log')
    #write to log
    with open(log_iot, mode='w', encoding='utf-8',newline='') as f:
        f.write('time,humidity,temperature\n')
else:
    print ('iot.log exists')
    #append to log
    with open(log_iot, mode='a', encoding='utf-8',newline='') as f:
        f.write(f"{time},{humidity},{celsius}\n")
    print ('new log is recorded')                