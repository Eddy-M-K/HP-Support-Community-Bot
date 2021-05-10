from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 
from selenium.common.exceptions import NoSuchElementException

# Function which returns the URL of the Product Specifications

def Product_Specifications_Link(driver, identifier):
    time.sleep(2)
    product_information = driver.find_element_by_id('tab-product-info')
    product_information.click()
    time.sleep(2)

    driver.implicitly_wait(10)
    dropdown = driver.find_element_by_id("dd-727118134876361637267272859691104_dd_headerLink")
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    driver.execute_script("arguments[0].click();", dropdown)

    driver.implicitly_wait(10)
    dropdown_product_specifications = driver.find_element_by_xpath("//ul[@id='dd-727118134876361637267272859691104_dd_list']/li[2]/a")
    dropdown_product_specifications.click()

    time.sleep(2)
    driver.implicitly_wait(10)
    try:
        product_specifications_text = driver.find_element_by_xpath("//div[@id='dd-items_727118134876361637267272859691104']/div/ul/li/a/*[contains(text(), '%s')]" % identifier)
        driver.execute_script("arguments[0].scrollIntoView();", product_specifications_text)
        driver.execute_script("arguments[0].click();", product_specifications_text)
        driver.switch_to.window(driver.window_handles[3])

        return driver.current_url
    except NoSuchElementException:
        return None

# Function which adds the information pertaining to the Product Specifications to the final answer

def Product_Specifications_Answer(driver, device, keywords, url, full_product_name):
    device.final_answer += '<hr /><p><font size="5"><strong>Product Specifications</strong></font></p>'
    
    device.final_answer += "<table><tbody>"
    content = driver.find_elements_by_class_name('content')
    table = content[0].find_element_by_xpath(".//div/div/table/tbody")

    if keywords == "all":
        full_table = content[0].find_element_by_xpath(".//div/div/table")
        tableHTML = full_table.get_attribute('innerHTML')
        device.final_answer += tableHTML
        device.final_answer += "</table>"
        device.final_answer += '<p>&nbsp;</p><p class="lia-align-center"><span><a href="%s" target="_blank" rel="noopener">Specifications Source</a></span></p>' % url
        return 
    else:
        for keyword in keywords: 
            keyword_row = table.find_element_by_xpath(".//*[contains(text(), '%s')]" % keyword)
            row = keyword_row.find_element_by_xpath(".//../../..")
            rowHTML = row.get_attribute('outerHTML')
            device.final_answer += rowHTML

        device.final_answer += "</table></tbody>"
        device.final_answer += '<p>&nbsp;</p><p class="lia-align-center"><span><a href="%s" target="_blank" rel="noopener">Specifications Source</a></span></p>' % url
        return