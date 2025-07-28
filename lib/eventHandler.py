import os
import time
from enum import Enum

'Enumeration for assigning Months from files to integers'
class Months(Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12

'Class definition for event to move information arround easily'
class event:
    def __init__(self, eventTitle, eventMonth, eventDay, eventYear, eventHour, eventMinute):
        self.title  = eventTitle
        self.month  = eventMonth
        self.day    = eventDay
        self.year   = eventYear
        self.hour   = eventHour
        self.min    = eventMinute


'This section will return the path to the "events" directory'
dir_events = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'events')

'This will take all files in the directory and assign it to "events_list_raw"'
events_list_raw = os.listdir(dir_events)

'This will create the list, and then iterates through the raw list to index all files into the list'
events_list = {}

for i in events_list_raw:
    events_list[events_list_raw.index(i)] = i

event0_dateandtime, event0_name = events_list[0].split(";")

'token_event_0_2 = token_event_0.split(",")'

event0_date, event0_time = event0_dateandtime.split("at")

calendarEvents = []



if __name__ == '__main__':
    """
    for i in events_list:
        print(f"{events_list[i]}")


    print("Event: " + event0_name + "\nDate: " + event0_date + "\nTime: " + event0_time)
"""
    


