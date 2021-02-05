# WhatsApp Web Automation

## Overview 
This project is developed to automate the process of wishing birthdays on WhatsApp web. It uses [selenium web-driver](https://www.selenium.dev) to run [firefox browser](https://www.mozilla.org/en-US/firefox/new/) in headless mode everyday at midnight to check birthdays of contacts from a csv file and wishes the contacts if there is a match.

## Table of contents
- [Requirements](#requirements)
- [Automating the script](#automating_the_script)

<a name="requirements"/>

## Requirements
This project requires you to have the following:

- [Python 2.7+](https://www.python.org/downloads/)
- [Selenium web-driver](https://pypi.org/project/selenium/)

<a name="automating_the_script"/>

## Automating the script
This project depends on the automation of the execution of the python script to be considered fully automated. This can be achieved by replicating the following steps 

- **For macOS**
  - Use the provided [plist](https://github.com/thisismayanktiwari/whatsapp_web_automation/blob/main/local.python.whatsappbday.plist) to create a [launchd](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html) process in macOS.
  
  **Note:** The plist provided runs everyday at midnight and can be transformed to work at some other time/interval as well.

- **For Windows**
  - Create a python executable file (bat file) and configure a task in the Task Scheduler. Read more about it [here](https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279).
  
- **For linux**
  - Open up the terminal and set up a jon in crontab. Learn how to set up a cron job [here](https://opensource.com/article/17/11/how-use-cron-linux).
  
