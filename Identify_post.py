from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Edge(r"C:\Users\EddyM\Downloads\edgedriver_win64 (1)\msedgedriver.exe")

driver.get('https://h30434.www3.hp.com/t5/Notebook-Boot-and-Lockup/Where-to-find-hard-drive-size/m-p/7954960/highlight/true#M196950')

driver.implicitly_wait(10)
accept = driver.find_element_by_id('onetrust-accept-btn-handler')
accept.click()

post_url = driver.current_url
split_url = post_url.split("/")

for url in split_url:
    if (url.isdigit()):
        post_number = url
        break 

post = driver.find_element_by_xpath("//div[@data-lia-message-uid='%s']" % post_number) #get number from end of url
driver.execute_script("arguments[0].scrollIntoView();", post)

#find mention and requested commands here

reply = post.find_element_by_xpath(".//a[@class='lia-button lia-button-secondary reply-action-link lia-action-reply']")
#actions = ActionChains(driver)
#actions.move_to_element(reply).perform()
driver.execute_script("arguments[0].scrollIntoView();", reply)
driver.execute_script("arguments[0].click();", reply)
#coordinates = reply.location_once_scrolled_into_view
#driver.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
#driver.execute_script("window.scrollTo(0, 1000)") 

username = driver.find_element_by_id("username")
username.send_keys('Eddy.M.K')

next_button = driver.find_element_by_id("next_button")
next_button.click()

time.sleep(1)
password = driver.find_element_by_id("password")
password.send_keys('iWwlY#0#W94RA4')

submit_button = driver.find_element_by_css_selector("button[type='submit']")#driver.find_element_by_class_name("vn-button vn-button--critical vn-button--expanded")
submit_button.click()
'''
profile = driver.find_element_by_link_text('/t5/user/viewprofilepage/user-id/3992734')
driver.execute_script("arguments[0].scrollIntoView();", profile)
commands = profile.text()
'''