from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 

def Input_Submit(driver, device):
    HTML_button = driver.find_element_by_id("mceu_26")
    driver.execute_script("arguments[0].scrollIntoView();", HTML_button)
    driver.execute_script("arguments[0].click();", HTML_button)

    driver.implicitly_wait(5)
    input_box = driver.find_element_by_id("mceu_254")
    input_box.send_keys(device.final_answer)

    ok_button = driver.find_element_by_id("mceu_256-button")
    ok_button.click()

    preview_button = driver.find_element_by_id("previewButton")
    preview_button.click()

    #post_button = driver.find_element_by_id("submitContext_0")
    #post_button.click()