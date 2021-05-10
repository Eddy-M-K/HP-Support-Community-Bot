from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 
from selenium.common.exceptions import NoSuchElementException

# Open the URL

def Open_URL(driver, url):
    driver.get('%s' % url)

# Close the URL and switch to browser tab 3

def Close_Current_Tab(driver):
    driver.close()
    driver.switch_to.window(driver.window_handles[2])