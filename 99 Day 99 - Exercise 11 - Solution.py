# Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system

import pymsgbox
import time

REPEAT_INTERVAL = 3600  # Repeat frequency in seconds

while True:
    # Display the message box
    pymsgbox.alert("Hey, Drink water!", "Water Reminder")

    # Pause execution for the repeat interval
    time.sleep(REPEAT_INTERVAL)