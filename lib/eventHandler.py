import os
import time
from enum import Enum
from datetime import datetime


# This section will return the path to the "events" directory
#   From inner most parenthesis, realpath gets the current pathway, dirname gets parent pathway, 
#   dirname gets parent pathway, join appends string to pathway
dir_events = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'events')

# This will take all files in the directory and assign it to "events_list_raw"
file_events_list = os.listdir(dir_events)

# Creates empty list to hold all files
events_list_raw = []

# For each file in event directory, add it to the events_list_raw list
for file in file_events_list:
    events_list_raw.append(file)

# String that follows format that is provided from iOS shortcuts
date_time_str_file_format = "%b %d, %Y at %I:%M %p"

# List that will contain all events
events_list = []

# Iterates through raw file names, splits datetime and names, strips the unknown char, then extracts the datetime object from strings, 
#   then adds to events list
for raw_event in events_list_raw:
    rawEventDate, EventName = raw_event.split(";")
    eventDate = datetime.strptime(rawEventDate.strip("\u202f"), date_time_str_file_format)
    events_list.append((eventDate, EventName))

# Sorting events list base upon the date, which is the "2nd" item in a tuple
events_list.sort(key=lambda date: date[0])

# Gets current datetime
currDate = datetime.today()

# Below will be used to remove old events
"""
def rmOldEvents(dir_img):
    for item in os.listdir(dir_img):
        if item.startswith('img_'):
            os.remove(os.path.join(dir_img, item))
        if item.startswith('tmp'):
            os.remove(os.path.join(dir_img, item))
"""

tmp = "%a %b %d, %Y  %I:%M %p"

f1 = "%Y-%m-%dT%H:%M:%S%z"
f2 = "%Y-%m-%d"
"""
if len(cal_list[i]) > 10:
#print(len(cal_list[i]))
  out = datetime.datetime.strptime(s, f1).strftime("%b %-d @ %-I:%M%p")
else:
  out = datetime.datetime.strptime(s, f2).strftime("%b %d")
  """





if __name__ == '__main__':

    print(events_list_raw)

    for events in events_list:
        if events[0] > currDate:
            print(f"{events[1]} {events[0].strftime(f2)}")

    print(f"\n{currDate}")
    
    #print("Index: " + str(events_list.index(events)) + "\nName: " + events[1] + "\nDate and Time: " + events[0].strftime(f1) + "\n\n")
    
    
    