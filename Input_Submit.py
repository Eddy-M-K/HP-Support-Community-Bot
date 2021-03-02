from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 
from selenium.common.exceptions import NoSuchElementException

def Input_Submit(driver, device):
    driver.implicitly_wait(5)
    ellipsis = driver.find_element_by_id("mceu_16-button")
    driver.execute_script("arguments[0].scrollIntoView();", ellipsis)
    driver.execute_script("arguments[0].click();", ellipsis)

    HTML_button = driver.find_element_by_id("mceu_27")
    driver.execute_script("arguments[0].scrollIntoView();", HTML_button)
    driver.execute_script("arguments[0].click();", HTML_button)

    time.sleep(1)
    box = driver.find_element_by_xpath("//div[@class='mce-container mce-panel mce-floatpanel mce-window mce-in']")
    input_box = box.find_element_by_xpath(".//textarea[@class='mce-textbox mce-multiline mce-abs-layout-item mce-first mce-last']")
    #input_box = driver.find_element_by_id("mceu_61")
    input_box.send_keys(device.final_answer)

    #ok_button = driver.find_element_by_id("mceu_63-button")
    ok_button = driver.find_element_by_id("mceu_63-button")
    ok_button.click()

    time.sleep(3)
    preview_button = driver.find_element_by_id("previewButton")
    driver.execute_script("arguments[0].scrollIntoView();", preview_button)
    driver.execute_script("arguments[0].click();", preview_button)

    try:
        driver.implicitly_wait(5)
        exit_preview_button = driver.find_element_by_id("exitPreviewButton")
        driver.execute_script("arguments[0].scrollIntoView();", exit_preview_button)
        driver.execute_script("arguments[0].click();", exit_preview_button)
    except NoSuchElementException:
        pass

    try:
        driver.implicitly_wait(5)
        preview_button = driver.find_element_by_id("previewButton")
        driver.execute_script("arguments[0].scrollIntoView();", preview_button)
        driver.execute_script("arguments[0].click();", preview_button)
    except NoSuchElementException:
        pass

    post_button = driver.find_element_by_id("submitContext_0")
    post_button.click()

    time.sleep(2)

    return