from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.common.exceptions import NoSuchElementException
from Sign_In_Notifications import *
from mySQL import *
from Identify_Post_and_Country import *
from Return_Commands import *
from Command_Type import *
from Software_and_Drivers import *
from Product_Specifications import *
from Main_Product_Page import *
from Open_Close import *

# Product Class Declaration + Definition
class Product:
    def __init__(self, driver, full_product_name, final_answer, software_link, specifications_link, maintenance_link):
        self.full_product_name = full_product_name
        self.final_answer = final_answer
        self.software_link = software_link
        self.specifications_link = specifications_link
        self.maintenance_link = maintenance_link

    def set_software_link(driver, software_link):
        self.software_link = Software_and_Drivers_Link(driver)

    def set_specifications_link(specifications_link):
        self.specifications_link = Product_Specifications_Link(driver)

    def set_maintenance_link(maintenance_link):
        self.maintenance_link = 

    def get_software_link():
        return self.software_link

    def get_specifications_link():
        return self.specifications_link

    def get_maintenance_link():
        return self.maintenance_link

    def sql_open_software(driver):

    def sql_open_specifications(driver):

    def sql_open_maintenance(driver):


# SQL Sign In and cursor object creation
s = open("mysql_signin.txt", "r")
user = s.readline()
password = s.readline()

db = mysql.connector.connect(
    host = "localhost",
    user = "%s" % user,
    password = "%s" % password,
    database = "HP"
)

mycursor = db.cursor()

# Web driver 
driver = webdriver.Edge(r"C:\Users\EddyM\Downloads\edgedriver_win64 (1)\msedgedriver.exe")
driver.get('https://h30434.www3.hp.com/t5/notificationfeed/page')

# Declares the Product dictionary, which will act as a list of Product instances
Product = {}

# Signs into the support community
Sign_In_Notifications(driver)

# Finds unread mentions
notification_list = driver.find_element_by_id("notificationList")
ul = notification_list.find_element_by_xpath(".//ul")
unread_mention_list = ul.find_elements_by_xpath(".//li[@class='lia-notification-feed-item lia-notification-mentions lia-component-notificationfeed-widget-notification-feed-item']") #lia-notification-feed-item lia-notification-mentions lia-notification-unread lia-component-notificationfeed-widget-notification-feed-item

# Loops through unread mentions
for mention in unread_mention_list:
    user_element = mention.find_element_by_xpath(".//div/div/div[2]/div/span")
    driver.execute_script("arguments[0].scrollIntoView();", user_element)
    user_text = user_element.text

    # Checks if the user is EddyK
    if user_text == 'EddyK': 
        # Opens forum thread with unread mention in new tab
        forum_thread_link = mention.find_element_by_xpath(".//div/div/div[2]/div/a")
        forum_thread_link.send_keys(Keys.CONTROL + Keys.ENTER)
        driver.switch_to.window(driver.window_handles[1])

        # Returns the country of the original poster, if available, and clicks on 'Reply' of the post containing the unread mention
        country = Identify_Post_and_Country(driver)

        # Returns the full command from the mention
        full_command = Return_Commands(driver)

        # Checks if the command is only a support command
        if (len(full_command.split(" ")) == 1):
            #Support Function Only
            pass
        else:
            # Finds the 
            split_commands = full_command.split(",")
            for x in range(len(split_commands)):
                if Command_Type(split_commands[x]) == 1:
                    identifier = split_individual_command[x + 1]
                    break

            full_product_name, final_answer = Main_Product_Page(driver, identifier, final_answer)

            if Check_If_Exist(mycursor, full_product_name):
                software_link, specifications_link, maintenance_link = SQL_Get_Links(mycursor)
                Product[identifier] = Product(driver, full_product_name, None, software_link, specifications_link, maintenance_link)

            else:
                Product[identifier] = Product(driver, full_product_name, None, None, None, None)
                Product[identifier].set_software_link(Software_and_Drivers_Link(driver))


            '''
            if full_product_name exists in database:

            else: 

            '''
            #Check if it already exists in database
            #If yes, create new device instance with the links as initialization
            #If no, create the instance, run all the methods, add to final_answer for requested commands, and store the links into the databse