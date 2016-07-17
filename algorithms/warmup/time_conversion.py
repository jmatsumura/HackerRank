#!/bin/python3

import sys, re

time = input().strip()
hours = re.search(r"(.*):.*:.*[A|P]M", time)
finalhours = 0
minutes = re.search(r".*:(.*):.*[A|P]M", time)
seconds = re.search(r".*:.*:(.*)[A|P]M", time)
nightday = re.search(r".*:.*:.*([A|P]M)", time)
if nightday.group(1) == 'PM':
    finalhours = int(hours.group(1)) + 12
    if finalhours == 24:
        finalhours = 12
else:
    finalhours = hours.group(1)
    if hours.group(1) == '12':
        finalhours = '00'
print("{}:{}:{}".format(finalhours, minutes.group(1), seconds.group(1)))
