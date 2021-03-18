from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Created By: Ryan Hong
March 2021
Open-Source - Have fun :)

'''

# open login page for Fit4Less in max screen size
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
browser.get(('https://myfit4less.gymmanager.com/portal/login.asp'))

# username and password --> change to your credentials
usernameStr = 'jodi.hong@hotmail.com'
passwordStr = 'happy1022'

username = browser.find_element_by_id('emailaddress')
username.send_keys(usernameStr)

password = browser.find_element_by_id('password')
password.send_keys(passwordStr)

# using loginButton.click() doesn't work on smaller screen dimensions as other elements cover the button
# using execute_script solves this issue --> basically makes this bot more dynamic/responsive
loginButton = browser.find_element_by_id('loginButton')
browser.execute_script("arguments[0].click();", loginButton)

browser.implicitly_wait(5)

# currently hardcoded to book at a specific date and time
dateButton = browser.find_element_by_id('btn_date_select')
browser.execute_script("arguments[0].click();", dateButton)

selectDate = browser.find_element_by_id('date_2021-03-21')
browser.execute_script("arguments[0].click();", selectDate)

selectTime = browser.find_element_by_xpath(
    "//div[@data-slottime = 'at 5:00 PM']")
browser.execute_script("arguments[0].click();", selectTime)

yesButton = browser.find_element_by_id('dialog_book_yes')
browser.execute_script("arguments[0].click();", yesButton)
