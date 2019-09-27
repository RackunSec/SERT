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
# Custom user-defined classes:
class Color:
    red = '\033[91m'
    blue = '\033[94m'
    green = '\033[92m'
    rst = '\033[0m'
color = Color()
# Custom user-defined functions:
def usage():
    print(color.red+"[ERROR] Usage: ... "+color.rst)
def hello():
    print(color.green+"\nSERT, Spirion EnCase Reporting Tool\n"+color.rst)
# Workflow:
hello()
if len(sys.argv) == 4:
    # Do stuff
    print("[msg] Got "+color.green+sys.argv[1]+color.rst+" for the Spirion file.")
    print("[msg] Got "+color.green+sys.argv[2]+color.rst+" as the evidence mount point.")
    print("[msg] Got filetype of "+color.green+sys.argv[3]+color.rst+" for the report.\n")
    with open(sys.argv[1],"r") as csv_file:
        for line in csv_file:
            # remove new line:
            line = line.rstrip('\n')
            # switch \ to /
            line = re.sub(r'\\','/',line)
            # remove PATH drive:
            line = re.sub('^[A-Za-z]:','',line)
            # Check if file exists in EnCase evidence mount point

            print "o: "+line
    csv_file.close()
else:
    usage()
