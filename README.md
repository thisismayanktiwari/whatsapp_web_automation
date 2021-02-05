# WhatsApp Web Automation

## Overview 
This project is developed to automate the process of wishing birthdays on WhatsApp web. It uses [selenium web-driver](https://www.selenium.dev) to run [firefox browser](https://www.mozilla.org/en-US/firefox/new/) in headless mode everyday at midnight to check birthdays of contacts from a csv file and wishes all the contacts it finds a match for.

**Note:** It is essential for you to be logged into your WhatsApp web for this project to work.

With a few tweaks here and there, this can be used with the browser of your choice and for purposes other than wishing birthdays like sending score updates, weather updates, stock price updates etc. It can be made to run every few minutes, every few hours, or even every few days (requires making changes to how you [automate the script](#automating_the_script)).

## Table of contents
- [Requirements](#requirements)
- [Automating the script](#automating_the_script)
- [Format of the csv file](#csv_format)

<a name="requirements"/>

## Requirements
This project requires you to install the following:

- [Python 2.7+](https://www.python.org/downloads/)
- [Selenium web-driver](https://pypi.org/project/selenium/)

<a name="automating_the_script"/>

## Automating the script
This project depends on the automation of the execution of the python script to be considered enitrely automated. This can be achieved by replicating the following steps: 

- **For macOS**
  - Use the provided [plist](https://github.com/thisismayanktiwari/whatsapp_web_automation/blob/main/local.python.whatsappbday.plist) to create a [launchd](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html) process in macOS.
  
  **Note:** The plist provided runs everyday at midnight and can be transformed to work at some other time/interval as well.

- **For Windows**
  - Create a python executable file (bat file) and configure a task in the Task Scheduler. Read more about it [here](https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279).
  
- **For linux**
  - Open up the terminal and set up a job in crontab. Learn how to set up a cron job [here](https://opensource.com/article/17/11/how-use-cron-linux).
  
<a name="csv_format"/>

## Format of the csv file
For this project to work, it is essential to follow the exact csv file format as shown below. Since the code adds "Happy Birthday" by itself, we only need to store the message we want to write after "Happy Birthday".

```
name,birth_month,birth_day,birth_msg #This line is essential and must be on top
John Doe,2,15,buddy 
Jane Doe,5,23,Jane
Sister Doe,3,4,sis
... and so on
```
