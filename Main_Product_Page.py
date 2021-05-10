from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

# Function to open the Main Product Page

def Main_Product_Page(driver, identifier, final_answer):
    driver.execute_script('''window.open("https://support.hp.com/us-en/products","_blank");''')

    driver.switch_to.window(driver.window_handles[2])

    search_box = driver.find_element_by_id('search-input-pfinder')
    search_box.send_keys(identifier)

    find_button = driver.find_element_by_id('btnSplitSearchSubmit')
    find_button.click()

    driver.implicitly_wait(10)
    full_product_name = driver.find_element_by_xpath("//div[@id='pdpPrdctHeading']/h2").text

    try:
        x_button = driver.find_element_by_id("dismiss-notifications")
        x_button.click()
    except NoSuchElementException:
        pass

    final_answer += '<p><font size="6"><strong><font face="hpsimplifiedlight,arial,sans-serif">%s</font></strong></font></p>' % full_product_name

    return full_product_name, final_answer

# Function to close intrusive popups that would interefere with the bot (Only runs once at the beginning)

def Main_Product_Page_Close(driver):
    driver.execute_script('''window.open("https://support.hp.com/us-en/products","_blank");''')
    driver.switch_to.window(driver.window_handles[1])

    driver.implicitly_wait(5)
    feedback_button = driver.find_element_by_id("opt_custom_Feedback")
    feedback_button.click()

    WebDriverWait(driver, 90).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='kampyleForm32024']")))
    driver.implicitly_wait(5)
    close = driver.find_element_by_xpath("//button[@ng-if='isShowFormCloseButton()']")
    close.click()

    driver.switch_to_default_content()

    driver.close()

    driver.switch_to.window(driver.window_handles[0])   

    return
