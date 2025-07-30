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
"""
n=Months.Jul
print(n.value)
This will output 7
"""


'Class definition for event to move information arround easily'
class event:
    def __init__(self, eventName, eventMonth, eventDay, eventYear, eventHour, eventMinute):
        self.name  = eventName
        self.date   = { 'month' : eventMonth,
                        'day'   : eventDay,
                        'year'  : eventYear}
        self.time   = { 'hour'  : eventHour,
                        'minute': eventMinute}




'This section will return the path to the "events" directory'
'   From inner most parenthesis, realpath gets the current pathway, dirname gets parent pathway, '
'   dirname gets parent pathway, join appends string to pathway'
dir_events = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'events')

'This will take all files in the directory and assign it to "events_list_raw"'
events_list_raw = os.listdir(dir_events)

'Creates empty list to hold all files'
events_list = {}

'For each file in raw list, make each index of raw list equal a new item in real list'
for i in events_list_raw:
    events_list[events_list_raw.index(i)] = i


"""

'Datetime and Title split'
event0_dateandtime, event0_name = events_list[0].split(";")

'Date and time split'
event0_date, event0_time = event0_dateandtime.split("at")

event0_monthday, event0_year = event0_date.split(",")

event0_month, event0_day = event0_date.split(",")

event0 = event(event0_name, event0_month.strip(), event0_day.strip(), "","","")

calendarEvents = []

calendarEvents.append(events_list[0])

"""



if __name__ == '__main__':
    """
    for i in events_list:
        print(f"{events_list[i]}")


    print("Event: " + calendarEvents[0].name)
    print("\nMonth: " + calendarEvents[0].date['month'])
    print("\nYear: " + calendarEvents[0].date['day'])

"""
    
    events_list0 = events_list[0].split(",")

    'Splits Month and Day'
    date_monthday = events_list0[0].split(" ")

    'Splits Year and etc.'
    date_list = events_list0[1].split("at")

    'Splits time and name'
    date_list0 = date_list[1].split(";")

    'Leaves just time'
    time_list = date_list0[0].strip("\u202f")

    print(events_list0)
    print(date_monthday)
    print(date_list)
    print(date_list0)
    print(time_list)

