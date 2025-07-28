# Animal Crossing ePaper Display Calendar
This is a hobby/project that I am making for my girlfriend. The goal is to create an *Animal Crossing Themed* Calendar ePaper/eInk display that I was given by an old job (i.e., they had a bunch of old broken screens and I was allow to bring it home). <br />

This is the second go at creating this calendar. Previously, I had it working for about 1 month, then 3 weeks, then 2 weeks, then 4 days at a time. The main hurdle has been Google's Cloud environment that allows you to access their servers. I had integrated it with my Gf's Google account, which worked, until it didnt. For this go around, I will be excluding Google and moving to Shortcuts from iOS which allows me to SSH into the pi. <br /> 

Fortunately, the ePaper PiHAT I purchased from Waveshare provides a link to their github which provides a variety of different initializations and drivers for ePaper displays. This allowed much of the nitty gritty coding to be a simple copy-paste as it is pre-existing is open-source and free to use without a license. <br />

## Current progress
Since this is the second attempt at making this system work, there are a few items I would like to include and plan to work on:
 - eventHandler.py -> This will handle the events created by Shortcuts on my phone
 - Remove Google Cloud -> I will need to rewrite the main functions of the system to remove this ability
 - Correct the various issues with the displays on the screen

## Main library test scripts
These Python Modules were created in V1.0 and I believe they may remain as is.
<br />

### driverConfig.py
This initializes and creates the ePaper connection to the Raspberry Pi via SPI protocol.

### initEPD7in5.py
This initalizes the ePaper display, creates functions to clear the screen, display to the screen, sleep the screen, etc..

### cal_ender.py
This creates the little calendar icon that appears on the ePaper display.

### API_nook.py
This is the API call to the nookpedia website where the islanders names and images are pulled from.

### imgConvertor.py
This takes the islanders and makes their images display more clearly on the ePaper display.

## main.py
This puts all the pieces of the pie together. It will call the functions from the **driverConfig**, **initEPD7in5** to clear the screen. Then it will call the **API_nook** to get the images downloaded and names of islanders, and also call **cal_ender** to create all the images required. Finally, it will put it altogether on the display in a clear and easy to read display.

