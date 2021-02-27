from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.common.exceptions import NoSuchElementException

def Maintenance_and_Service_Guide():
    #driver.switch_to.window(driver.swindow_handles[2])

    manuals = driver.find_element_by_id('manuals')
    manuals.click()

    maintenance_and_service_guide_text = driver.find_element_by_xpath("//tbody[@id='userGuidesList']/tr/td/a/*[contains(text(), 'Maintenance and Service Guide')]")
    driver.execute_script("arguments[0].scrollIntoView();", maintenance_and_service_guide_text)
    driver.execute_script("arguments[0].click();", maintenance_and_service_guide_text)
    maintenance_and_service_guide_page = maintenance_and_service_guide_text.find_element_by_xpath('..').get_attribute('href')
    
    driver.switch_to.window(driver.window_handles[1])

    driver.close()

    driver.switch_to.window(driver.window_handles[0])

    #<hr /><p><font size="5"><strong>Maintenance and Service Guide</strong></font></p>

    return maintenance_and_service_guide_page
'''
def Identify_Commands():
    post_url = driver.current_url
    split_url = post_url.split("/")

    for url in split_url:
        if '#' in url:
            string_hash = url.split("#")
            post_number = string_hash[0]
            break 

    post = driver.find_element_by_xpath("//div[@data-lia-message-uid='%s']" % post_number)
    driver.execute_script("arguments[0].scrollIntoView();", post)
    reply_button = post.find_element_by_xpath(".//a[@class='lia-button lia-button-secondary reply-action-link lia-action-reply']")
    driver.execute_script("arguments[0].scrollIntoView();", reply_button)
    driver.execute_script("arguments[0].click();", reply_button)
'''
Sign_In_Notifications(username, password)
model_name = "an015np"
full_product_name, main_product_page_url = Main_Product_Page(model_name)
print(Maintenance_and_Service_Guide())
print(Product_Specifications(model_name))
print("Success")
driver.quit()