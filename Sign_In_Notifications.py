from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 

def Sign_In_Notifications(driver):
    t = open("signin.txt", "r")
    id_username = t.readline()
    id_password = t.readline()

    driver.implicitly_wait(5)
    username = driver.find_element_by_id("username")
    username.send_keys(id_username)

    next_button = driver.find_element_by_id("next_button")
    next_button.click()

    time.sleep(1)
    password = driver.find_element_by_id("password")
    password.send_keys(id_password)

    submit_button = driver.find_element_by_css_selector("button[type='submit']")#driver.find_element_by_class_name("vn-button vn-button--critical vn-button--expanded")
    submit_button.click()

    driver.implicitly_wait(10)
    time.sleep(1)
    accept = driver.find_element_by_id('onetrust-accept-btn-handler')
    accept.click()

    close = driver.find_element_by_class_name("close")
    close.click()