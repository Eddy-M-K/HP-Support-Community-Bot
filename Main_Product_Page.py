from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 
from selenium.common.exceptions import NoSuchElementException

def Main_Product_Page(driver, identifier, final_answer):
    driver.execute_script('''window.open("https://support.hp.com/us-en/products","_blank");''')

    driver.switch_to.window(driver.window_handles[2])
    '''
    driver.implicitly_wait(10)
    accept = driver.find_element_by_id('onetrust-accept-btn-handler')
    accept.click()
    '''
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

    #<p><font size="6"><strong><font face="hpsimplifiedlight,arial,sans-serif">HP Spectre x360 - 13-ap0053dx</font></strong></font></p>
    final_answer += '<p><font size="6"><strong><font face="hpsimplifiedlight,arial,sans-serif">%s</font></strong></font></p>' % full_product_name

    return full_product_name, final_answer