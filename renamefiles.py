# Author: Taimur Khan
# Purpose: Renaming files in the order of which they were modified
# Date: 22 December 2019

import os
from os import path

# Get the working directory
working_dir = os.getcwd()

# Newest to oldest or oldest to newest can be set using this boolean
newest_to_oldest = False

# Init the dictionary of times
dic_times = {}

# Iterate through a loop, finding all files in the working directory
# Use os.path to get the modify time and set that as a key with the value
# being the files name in the dictionary
for f, r, d in os.walk(working_dir):
    if f == working_dir:
        for x in d:
            if x != 'renamefiles.py':
                dic_times[path.getmtime(x)] = x

# Create a list of the sorted times
sorted_times = sorted(dic_times.keys())

# Reverse that list if the newest to oldest boolean is true
if newest_to_oldest:
    sorted_times = reversed(sorted_times)

# Init a counter for the file names
counter = 1

# For each of the times in the sorted times,
# find the corresponding value in the dictionary
# and set it to be equal to the index of the time in the sorted list +1
for x in sorted_times:
    ext = path.splitext(dic_times[x])[1]
    os.rename(working_dir + "\\" + dic_times[x], working_dir + "\\" + str(counter) + ext)
    dic_times[x] = counter
    counter += 1
