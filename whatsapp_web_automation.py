from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import csv
from datetime import date

def browser(fname, fmsg):
    ffoptions = Options()
    ffoptions.headless = True
    prof = '/Users/........../Firefox/Profiles/oy8jjdam.default-release'
    # prof stores the path to the firefox profile used to log into whatsapp web
    # Check out the following webpage to find your profile- 
    # https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data#w_how-do-i-find-my-profile
    driver = webdriver.Firefox(firefox_profile=prof, options=ffoptions, executable_path= '/usr/local/bin/geckodriver', service_log_path='/Users/....../Developer/Python/....../geckodriver.log')
    # executable_path stores the location of geckodriver
    # service_log_path is used to store the location where you want to save geckodriver logs
    driver.get('https://web.whatsapp.com')
    elem_search = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//div[@class="_3FRCZ copyable-text selectable-text" and @data-tab="3" and @dir="ltr" and @contenteditable="true"]')))
    elem_search.send_keys(fname)
    elem_name = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//span[@class="matched-text _3Whw5"]')))
    elem_name.click()
    elem_msg = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//div[@class="_3FRCZ copyable-text selectable-text" and @data-tab="1" and @dir="ltr" and @spellcheck="true" and @contenteditable="true"]')))
    elem_msg.click()
    elem_msg.send_keys("Happy Birthday " + fmsg + "!!")
    elem_msg.send_keys(Keys.RETURN)
    driver.quit()

def check():
    month = date.today().month
    day = date.today().day
    contacts_csv = '/Users/........Developer/contacts_csv.csv'
    # contacts_csv is used to store the path to the csv file to your contacts. Find more information about contacts_csv in README.md
    with open(contacts_csv, 'r') as bdays:
        reader = csv.reader(bdays)
        next(reader)
        for row in reader:
            if int(row[1])==month and int(row[2])==day:
                browser(row[0], row[3])

if __name__ == '__main__':
    check()