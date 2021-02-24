from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver = webdriver.Edge(r"C:\Users\EddyM\Downloads\edgedriver_win64 (1)\msedgedriver.exe")

driver.get('https://support.hp.com/us-en/product/hp-spectre-13-ap0000-x360-convertible-pc/23238155/model/27939992/product-info')

driver.implicitly_wait(10)
accept = driver.find_element_by_id('onetrust-accept-btn-handler')
accept.click()

dropdown = driver.find_element_by_id("dd-727118134876361637267272859691104_dd_headerLink")
dropdown.click()

product_specifications = driver.find_element_by_xpath("//ul[@id='dd-727118134876361637267272859691104_dd_list']/li[2]/a")
product_specifications.click()