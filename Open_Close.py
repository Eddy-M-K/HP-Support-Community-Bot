from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 
from selenium.common.exceptions import NoSuchElementException

def Open_New_Tab(driver, url):
    driver.execute_script('''window.open("%s","_blank");''' % url)

def Close_Current_Tab(driver):
    driver.close()
    driver.switch_to.window(driver.window_handles[2])