from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Created By: Ryan Hong
March 2021
Open-Source - Have fun :)

'''

# open login page for Fit4Less
browser = webdriver.Chrome()
browser.get(('https://myfit4less.gymmanager.com/portal/login.asp'))

# username and password --> change to your credentials
usernameStr = 'your email here'
passwordStr = 'your password here'

username = browser.find_element_by_id('emailaddress')
username.send_keys(usernameStr)

password = browser.find_element_by_id('password')
password.send_keys(passwordStr)

loginButton = browser.find_element_by_id('loginButton')
loginButton.click()
