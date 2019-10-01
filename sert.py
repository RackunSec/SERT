#!/usr/bin/env python
# 2019 SERT, Spirion EnCase Reporting Tool
#
# 1. Extract the CSV of results from Spirion
# 2. Mount the E01 drive
# 3. Run sert.py
#  Args:
#   1) PATH to Spirion CSV
#   2) PATH to EO1 Directory
#   3) Type of report
#       a) CSV
#       b) JSON
import sys # for args
import re # for regexp
import os # for OS/FS utilities
import time # for timestamp conversion
import stat # for file stats
# Custom user-defined classes:
class Color:
    red = '\033[91m'
    blue = '\033[94m'
    green = '\033[92m'
    cyan = '\033[96m'
    yellow = '\033[93m'
    rst = '\033[0m'
color = Color()
# Custom user-defined functions:
def usage():
    print(color.red+"[ERROR] Usage: ... "+color.rst)
def hello():
    print(color.yellow+"\nSERT"+color.green+", Spirion EnCase Reporting Tool\n"+color.rst)
def brackets(string):
    bcolor=color.cyan
    if string == "ERROR":
        bcolor=color.red
    return color.yellow+"["+bcolor+string+color.yellow+"] "+color.rst
# Workflow:
hello()
if len(sys.argv) == 4:
    # open log file for writing:
    log = open(sys.argv[3]+"_"+str(int(time.time()))+".csv","a") # lol wtf is that thing?
    log.write("File Name,Last Modified,Last Accessed,Date Created\n") # Create CSV header
    # Do stuff
    print(brackets("msg")+"Got "+color.green+sys.argv[1]+color.rst+" for the Spirion file.")
    print(brackets("msg")+"Got "+color.green+sys.argv[2]+color.rst+" as the evidence mount point.")
    print(brackets("msg")+"Got filetype of "+color.green+sys.argv[3]+color.rst+" for the report.\n")
    piiFiles = [] # this is the files found in the Spirion CSV Export
    evidencePath=sys.argv[2] # Path to Mounted Evidence
    evidencePath=re.sub(r'/$','',sys.argv[2])
    evidencePathLen=len(evidencePath)
    try:
        with open(sys.argv[1],"r") as csv_file:
            for line in csv_file:
                # remove new line:
                line = line.rstrip('\n')
                # switch \ to /
                line = re.sub(r'\\','/',line)
                # remove PATH drive:
                line = re.sub('^[A-Za-z]:','',line)
                # Check if file exists in EnCase evidence mount point
                splitline = line.split(',')
                cleanLine = re.sub(r'\\','/',splitline[6])
                #cleanLine = cleanLine.replace(' ','\ ')
                cleannodrive = re.sub(r'^[A-Z]:','',cleanLine)
                if splitline[6] not in piiFiles and len(splitline[6]) > evidencePathLen:
                    piiFiles.append(evidencePath+cleannodrive) # track the file being processed
                    try:
                        info=os.stat(evidencePath+cleannodrive) # process the file and print the result:
                        result=splitline[6]+","+time.ctime(info[stat.ST_MTIME])+","+time.ctime(info[stat.ST_ATIME])+","+time.ctime(info[stat.ST_CTIME])+"\n"
                        print(result)
                        log.write(result) # log it ot the file.
                    except OSError,e:
                        print(brackets("ERROR")+str(e))
                        continue
        csv_file.close()
    except IOError,e:
        print(brackets("ERROR")+str(e)+"\n")
        # sys.exit() # DEBUG
else:
    usage()
