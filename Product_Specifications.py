from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.common.exceptions import NoSuchElementException

def Product_Specifications_Link(driver):
    #driver.switch_to.window(driver.window_handles[2])

    product_information = driver.find_element_by_id('tab-product-info')
    product_information.click()

    driver.implicitly_wait(10)
    dropdown = driver.find_element_by_id("dd-727118134876361637267272859691104_dd_headerLink")
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    driver.execute_script("arguments[0].click();", dropdown)

    dropdown_product_specifications = driver.find_element_by_xpath("//ul[@id='dd-727118134876361637267272859691104_dd_list']/li[2]/a")
    dropdown_product_specifications.click()

    driver.implicitly_wait(10)
    product_specifications_text = driver.find_element_by_xpath("//div[@id='dd-items_727118134876361637267272859691104']/div/ul/li/a/*[contains(text(), '%s')]" % model_name)
    driver.execute_script("arguments[0].scrollIntoView();", product_specifications_text)
    driver.execute_script("arguments[0].click();", product_specifications_text)

    driver.switch_to.window(driver.window_handles[3])

    link = driver.current_url

    return link

def Product_Specifications_Answer(driver, final_answer, keywords)

final_answer += "<table><tbody>"
    content = driver.find_elements_by_class_name('content')
    table = content[0].find_element_by_xpath(".//div/div/table/tbody")

    for keyword in keywords: 
        keyword_row = table.find_element_by_xpath(".//*[contains(text(), '%s')]" % keyword)
        row = keyword_row.find_element_by_xpath(".//../../..")
        rowHTML = row.get_attribute('outerHTML')
        answer += rowHTML

    final_answer += "</table></tbody>"

    return final_answer


driver.quit()