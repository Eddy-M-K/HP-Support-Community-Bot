from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.common.exceptions import NoSuchElementException
from Readfile import *
from Sign_In_Notifications import *
from Identify_Post_and_Country import *
from Return_Commands import *
from Command_Type import *
from Software_and_Drivers import *
from Product_Specifications import *
from Main_Product_Page import *

class Product:
    def __init__(self, driver, identifier, final_answer, software_link, specifications_link, maintenance_link, full_product_name):
        self.identifier = identifier
        self.final_answer = final_answer
        self.software_link = software_link
        self.specifications_link = specifications_link
        self.maintenance_link = maintenance_link
        self.full_product_name = full_product_name

    def set_software_link(driver):
        self.software_link = Software_and_Drivers_Link(driver)

    def set_specifications_link():
        self.specifications_link = Product_Specifications_Link(driver)

    def set_maintenance_link():

    def get_software_link():
        return self.software_link

    def get_specifications_link():
        return self.specifications_link

    def get_maintenance_link():
        return self.maintenance_link

driver = webdriver.Edge(r"C:\Users\EddyM\Downloads\edgedriver_win64 (1)\msedgedriver.exe")
driver.get('https://h30434.www3.hp.com/t5/notificationfeed/page')

username, password = Get_Sign_In()

final_answer = None

Sign_In_Notifications(driver, username, password)

notification_list = driver.find_element_by_id("notificationList")
ul = notification_list.find_element_by_xpath(".//ul")

unread_mention_list = ul.find_elements_by_xpath(".//li[@class='lia-notification-feed-item lia-notification-mentions lia-component-notificationfeed-widget-notification-feed-item']") #lia-notification-feed-item lia-notification-mentions lia-notification-unread lia-component-notificationfeed-widget-notification-feed-item

for mention in unread_mention_list:
    user_element = mention.find_element_by_xpath(".//div/div/div[2]/div/span")
    driver.execute_script("arguments[0].scrollIntoView();", user_element)
    user_text = user_element.text

    if user_text == 'EddyK': 
        forum_thread_link = mention.find_element_by_xpath(".//div/div/div[2]/div/a")
        forum_thread_link.send_keys(Keys.CONTROL + Keys.ENTER)
        driver.switch_to.window(driver.window_handles[1])

        country = Identify_Post_and_Country(driver)

        full_command = Return_Commands(driver)

        if (len(full_command.split(" ")) == 1):
            #Support Function Only
            pass
        else:
            split_commands = full_command.split(",")
            for x in range(len(split_commands)):
                if Command_Type(split_commands[x]) == 1:
                    identifier = split_individual_command[x + 1]
                    break

            full_product_name, final_answer = Main_Product_Page(driver, identifier, final_answer)
            '''
            if full_product_name exists in database:

            else: 

            '''
            #Check if it already exists in database
            #If yes, create new device instance with the links as initialization
            #If no, create the instance, run all the methods, add to final_answer for requested commands, and store the links into the databse