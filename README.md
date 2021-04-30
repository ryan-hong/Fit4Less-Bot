# Fit4Less-Bot

Pre-pandemic, there was never a problem with booking time-slots at my local Fit4Less gym. However, with new restrictions due to Covid-19, time-slots have become increasingly difficult to book as there a limited spots.

Now has never been a better time to create a bot that automates the booking process to ensure a time-slot for yourself. Noticing this booking problem, not only in myself, but with my friends as well, I believe this project will be to our benefit, and to anyone else who would like to utilize this tool. Being open-source, you are free to use this code and make changes to your liking. I hope you find it useful in some way.

This is a bot using Python and Selenium to automate the time-slot booking process. **It should be noted that the main purpose of this bot is to book the same workout time for every 2 days (since F4L only allows maximum of 2 time bookings). This bot should not be used if you plan to workout at different times throughout the week.**

Have fun.

# How to setup script

First, pip install selenium

Then download chromedriver, make sure it is in same directory as python script, if you git clone, then just replace the existing chromedriver.exe in the directory

# How to setup auto run on Windows

First, run the script (make sure to replace user crendential placeholder and also chromedriver.exe path placeholder)

If the browser pops up, and you see corresponding messages in console, then the script should be running fine - its a simple script so there shouldnt be any errors

**IMPORTANT: Workout time is hardcoded to be 6:00 PM - If you would like to change this, simply navigate to line 58 and change the 6:00 PM (at @date-slottime) to whatever time has a workout slotted. Bot also does not work if computer is shutdown.**

Once everything works manually follow the steps below to setup automatic script run (Windows only):

## Step 1: Create Batch File to Run Python Script

Open a notepad and fill in the following

```bash
"Path where your Python.exe is stored\python.exe" "Path where scrip is stored\login.py"
pause
```

Save the notepad as a **.bat** file - something like "run_login.bat" and save to any desired location

To verify this works, double-click your .bat file (in whichever directory you saved it in) and the script should run - If not, make sure your paths are correct


## Step 2: Schedule using Windows Task Scheduler

Open windows start menu, and search for Task Scheduler

Locate "Create Basic Task..." (usually on the right-hand side) and click

Name your task to whatever you want

Set "Trigger" to "Daily", click next

Set start time to whatever time you would like to book your workouts at

For example, for myself, I book workouts for 6:00 PM everyday, so I set my time to be 6:00 PM

Click next

Set "Action" to "Start a program", click next

Insert path of your .bat file, click next

Verify task details, click finish


## Step 3: Optional

If you don't plan on being near the computer or the computer may be in sleep mode you can set the task to wake your PC up to start the task

Simply navigate to your task in Task Scheduler, double click it

Go over to the "Conditions" tab and check the "Wake the computer to run this task" box

If you have a password on your account, go back to the "General" tab and select the "Run whether user is logged on or not" box and fill out credentials

Doing these steps will allow your task to run even if your computer is in sleep mode. **It will not run if your computer is shutdown.**

For a more complete guide: https://datatofish.com/python-script-windows-scheduler/
