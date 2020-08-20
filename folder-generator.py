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

# Create path name variables
today = datetime.datetime.today()
current_day = today.strftime('%Y_%m_%d')
current_day_RAW = "./" + current_day  + "/0-RAW"
current_day_jpeg = "./" + current_day  + "/1-jpeg"
current_day_video = "./" + current_day + "/2-video"
current_day_selects = "./" + current_day + "/3-selects"
current_day_export = "./" + current_day + "/4-export"
current_day_export_full = "./" + current_day + "/4-export" + "/full-size"
current_day_export_web = "./" + current_day + "/4-export" + "/web-size"

if os.path.exists(current_day):
    createFolder(current_day + "_1")

# Loop to generate folders every subsequent run
# print len([name for name in os.listdir('.') if os.path.isfile(name)])

createFolder(current_day)
createFolder(current_day_RAW)
createFolder(current_day_jpeg)
createFolder(current_day_video)
createFolder(current_day_selects)
createFolder(current_day_export)
createFolder(current_day_export_full)
createFolder(current_day_export_web)

# print(os.path.isdir(current_day))
# print(os.path.exists(current_day))

