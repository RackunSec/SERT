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
#
#
import sys
def usage():
    print "Usage: ... "
if len(sys.argv) == 4:
    # Do stuff
    print("OK")
else:
    usage()
