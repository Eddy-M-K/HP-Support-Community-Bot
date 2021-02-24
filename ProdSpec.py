from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.common.exceptions import NoSuchElementException

answer = "<table><tbody>"

driver = webdriver.Edge(r"C:\Users\EddyM\Downloads\edgedriver_win64 (1)\msedgedriver.exe")

driver.get('https://support.hp.com/ca-en/document/c06296486')

driver.implicitly_wait(10)
accept = driver.find_element_by_id('onetrust-accept-btn-handler')
accept.click()

keywords = ["Video", "External", "Audio"]

content = driver.find_elements_by_class_name('content')
table = content[0].find_element_by_xpath(".//div/div/table/tbody")

for keyword in keywords: 
    keyword_row = table.find_element_by_xpath(".//*[contains(text(), '%s')]" % keyword)
    row = keyword_row.find_element_by_xpath(".//../../..")
    rowHTML = row.get_attribute('outerHTML')
    answer += rowHTML

answer += "</table></tbody>"

print(answer)

driver.quit()