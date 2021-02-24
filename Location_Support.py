from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

#Must sign-in to work

driver = webdriver.Edge(r"C:\Users\EddyM\Downloads\edgedriver_win64 (1)\msedgedriver.exe")

driver.get('https://h30434.www3.hp.com/t5/Notebook-Software-and-How-To-Questions/Disable-Ambient-Light-Sensor-on-Elitebook-840-g7/m-p/7939316#M281537')

driver.implicitly_wait(10)
accept = driver.find_element_by_id('onetrust-accept-btn-handler')
accept.click()

time.sleep(2)
sign_in = driver.find_element_by_xpath("//ul[@class='UserNavigation user-anonymous-menus']/li[1]/a")
sign_in.click()

username = driver.find_element_by_id("username")
username.send_keys("Eddy.M.K")

next_button = driver.find_element_by_id("next_button")
next_button.click()

time.sleep(1)
password = driver.find_element_by_id("password")
password.send_keys("iWwlY#0#W94RA4")

submit_button = driver.find_element_by_css_selector("button[type='submit']")#driver.find_element_by_class_name("vn-button vn-button--critical vn-button--expanded")
submit_button.click()

user_location = driver.find_element_by_xpath("//div[@class='user-location-wrap']/span").text

driver.execute_script('''window.open("https://www8.hp.com/us/en/contact-hp/ww-contact-us.html","_blank");''')
driver.switch_to.window(driver.window_handles[1])

driver.implicitly_wait(10)
driver.find_element_by_xpath("//div[@class='accordion disabled']/h3[@class='trigger']/a[contains(text(), user_location)]")
