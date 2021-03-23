from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException
from datetime import datetime, timedelta

'''
Created By: Ryan Hong
March 2021
Open-Source - Have fun :)

'''

# open login page for Fit4Less in max screen size
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(
    executable_path=r'your chromedriver.exe path here', options=options)
browser.get(('https://myfit4less.gymmanager.com/portal/login.asp'))

# username and password --> change to your credentials
usernameStr = 'Your email here'
passwordStr = 'Your password here'

# no try-except-finally block for login, so make sure your credentials are correct
username = browser.find_element_by_id('emailaddress')
username.send_keys(usernameStr)

password = browser.find_element_by_id('password')
password.send_keys(passwordStr)

# using loginButton.click() doesn't work on smaller screen dimensions as other elements cover the button
# using execute_script solves this issue --> basically makes this bot more dynamic/responsive
loginButton = browser.find_element_by_id('loginButton')
browser.execute_script("arguments[0].click();", loginButton)

browser.implicitly_wait(5)

# get current date + 3 to book time 3 days in advance
now = datetime.now().date()
td = timedelta(days=3)
# convert datetime object to string
future = (now + td).strftime("%Y-%m-%d")
# format properly to match how web browser takes in date
formatDate = 'date_'+future
slotdate = (now + td).strftime("%A, %d %B %Y").lstrip("0").replace(" 0", " ")

# currently hardcoded to book at a specific date and time
try:
    dateButton = browser.find_element_by_id('btn_date_select')
    browser.execute_script("arguments[0].click();", dateButton)

    selectDate = browser.find_element_by_id(formatDate)
    browser.execute_script("arguments[0].click();", selectDate)

    selectTime = browser.find_element_by_xpath(
        "//div[@data-slotdate ='" + slotdate + "'][@data-slottime = 'at 6:00 PM' ]")
    browser.execute_script("arguments[0].click();", selectTime)

    yesButton = browser.find_element_by_id('dialog_book_yes')
    browser.execute_script("arguments[0].click();", yesButton)

    print("Booking Successfull - Check your email for confirmation!")

except (NoSuchElementException, ElementNotSelectableException):
    print("Date or time is unavailable to book")

finally:
    print("Bye!")
