import os
import time
from enum import Enum
from datetime import datetime


# Format 1 & 2 that will be displayed on Calendar
f1 = "%a, %b %d @ %I:%M%p"
f2 = "%a, %b %d"


def getEvents(event_directory):
    
    events_list_raw = []    # Creates empty list to hold all files
    events_list = []        # Creates empty list to hold all event names and dates/datetimes


    # String follows format that is provided from iOS Shortcuts
    date_time_str_file_format1 = "%b %d, %Y at %I:%M %p" 
    date_time_str_file_format2 = "%b %d, %Y" 

    print("flag 1")
    print(event_directory)

    # This will take all files in the directory and assign it to "events_list_raw"
    file_events_list = os.listdir(event_directory)

    print("flag 2")
    
    # For each file in event directory, add it to the events_list_raw list
    for file in file_events_list:
        events_list_raw.append(file)


    # Iterates through raw file names, splits datetime and names, strips the unknown char, 
    #   then extracts the datetime object from strings, then adds to events list
    for raw_event in events_list_raw:
        rawEventDate, EventName = raw_event.split(";")
        if len(rawEventDate) > 12:
            eventDate = datetime.strptime(rawEventDate.strip("\u202f"), date_time_str_file_format1)
            allDay = False
        else:
            eventDate = datetime.strptime(rawEventDate.strip("\u202f"), date_time_str_file_format2)
            allDay = True
        events_list.append((eventDate, EventName, allDay))

    return events_list


def sortEvents(list_of_events):
    list_of_events.sort(key=lambda date: date[0])
    return list_of_events

def events2strings(list_of_events):
    event_list_str = []
    for events in list_of_events:
        if events[2] == True:
            event = f"{events[1]} {events[0].strftime(f2)}"
        else:
            event = f"{events[1]} {events[0].strftime(f1)}"
        event_list_str.append(event)
    return event_list_str




# Below will be used to remove old events
"""
def rmOldEvents(dir_img):
    for item in os.listdir(dir_img):
        if item.startswith('img_'):
            os.remove(os.path.join(dir_img, item))
        if item.startswith('tmp'):
            os.remove(os.path.join(dir_img, item))
"""

# Only runs if main file is run (will not occur and is not brought to main)

if __name__ == '__main__':

    # Provides the pathway to the events directory
    dir_events = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'events')

    # Gets the events, sorts them, then converts them to the string format
    events_list = events2strings(sortEvents(getEvents(dir_events)))

    # Prints events in list to terminal
    for events in events_list:
        print(events)


    