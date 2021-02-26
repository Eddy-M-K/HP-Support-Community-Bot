from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.common.exceptions import NoSuchElementException
from Sign_In_Notifications import *
from Identify_Post_and_Country import *
from Return_Commands import *
from Command_Type import *

t = open("signin.txt", "r")
username = t.readline()
password = t.readline()

driver = webdriver.Edge(r"C:\Users\EddyM\Downloads\edgedriver_win64 (1)\msedgedriver.exe")
driver.get('https://h30434.www3.hp.com/t5/notificationfeed/page')

Sign_In_Notifications(driver, username, password)
'''
driver.implicitly_wait(10)
notification_list = driver.find_element_by_id("notificationList")
ul = notification_list.find_element_by_xpath(".//ul")

unread_mention_list = ul.find_elements_by_xpath(".//li[@class='lia-notification-feed-item lia-notification-mentions lia-component-notificationfeed-widget-notification-feed-item']") #lia-notification-feed-item lia-notification-mentions lia-notification-unread lia-component-notificationfeed-widget-notification-feed-item

for mention in unread_mention_list:
    user = mention.find_element_by_xpath(".//div/div/div[2]/div/span").text
    if user == 'EddyK': 
        forum_thread_link = mention.find_element_by_xpath(".//div/div/div[2]/div/a")
        forum_thread_link.send_keys(Keys.CONTROL + Keys.ENTER)
        driver.switch_to.window(driver.window_handles[1])

        country = Identify_Post_and_Country(driver)
        print(country)

        #full_command = Return_Commands()
        #print(full_command)

        split_commands = full_command.split(" ")
        for x in range(len(split_commands)):
            if command_type(split_command[x]) == 1:
                Main_Product_Page([x + 1])
            else:
'''