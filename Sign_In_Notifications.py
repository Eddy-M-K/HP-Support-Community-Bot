from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

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
    time.sleep(3)
    try:
        accept = driver.find_element_by_id('onetrust-accept-btn-handler')
        accept.click()
    except NoSuchElementException:
        pass

    close = driver.find_element_by_class_name("close")
    close.click()
    '''
    WebDriverWait(driver, 90).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='kampyleInvite']")))

    driver.implicitly_wait(90)
    not_right_now_button = driver.find_element_by_id("kplDeclineButton")
    not_right_now_button.click()

    driver.switch_to_default_content()
    '''
    driver.implicitly_wait(3)
    feedback_button = driver.find_element_by_class_name("opt-feedback-link")
    feedback_button.click()

    WebDriverWait(driver, 90).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='kampyleForm32024']")))
    driver.implicitly_wait(5)
    close2 = driver.find_element_by_xpath("//button[@ng-if='isShowFormCloseButton()']")
    close2.click()

    driver.switch_to_default_content()

    return