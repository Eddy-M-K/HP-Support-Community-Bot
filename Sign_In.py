from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver = webdriver.Edge(r"C:\Users\EddyM\Downloads\edgedriver_win64 (1)\msedgedriver.exe")

def Sign_In():
    driver.get('https://h30434.www3.hp.com/')

    driver.implicitly_wait(10)
    accept = driver.find_element_by_id('onetrust-accept-btn-handler')
    accept.click()

    time.sleep(2)
    sign_in = driver.find_element_by_xpath("//ul[@class='UserNavigation user-anonymous-menus']/li[1]/a")
    sign_in.click()

    username = driver.find_element_by_id("username")
    username.send_keys("HPDeviceHelper@outlook.com")

    next_button = driver.find_element_by_id("next_button")
    next_button.click()

    time.sleep(1)
    password = driver.find_element_by_id("password")
    password.send_keys("$0Wg5u29rS#9@E!")

    submit_button = driver.find_element_by_css_selector("button[type='submit']")#driver.find_element_by_class_name("vn-button vn-button--critical vn-button--expanded")
    submit_button.click()

Sign_In()