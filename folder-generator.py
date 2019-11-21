# Based from: https://gist.github.com/keithweaver/562d3caa8650eefe7f84fa074e9ca949
# Date time info: https://learnandlearn.com/python-programming/python-reference/python-get-current-date

# Works for python 3.8

import os
import datetime


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
today = datetime.datetime.today()
current_day = today.strftime('%Y_%m_%d')
current_day_RAW = "./" + current_day  + "/RAW"
current_day_selects = "./" + current_day + "/selects"
current_day_video = "./" + current_day + "/video"

if os.path.exists(current_day):
    createFolder(current_day + "_1")

# Loop to generate folders every subsequent run
# print len([name for name in os.listdir('.') if os.path.isfile(name)])

createFolder(current_day)
createFolder(current_day_RAW)
createFolder(current_day_selects)
createFolder(current_day_video)

# print(os.path.isdir(current_day))
# print(os.path.exists(current_day))

