from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.common.exceptions import NoSuchElementException
from Sign_In_Notifications import *
from mySQL_ProductLinks import *
from Identify_Post_and_Country import *
from Return_Commands import *
from Command_Type import *
from Product_Specifications import *
from Maintenance_and_Service_Guide import *
from Software_and_Drivers import *
from Main_Product_Page import *
from Open_Close import *
from Input_Submit import *

# Product Class Declaration + Definition
class Product:
    def __init__(self, driver, full_product_name, final_answer, software_link, specifications_link, maintenance_link):
        self.full_product_name = full_product_name
        self.final_answer = final_answer
        self.software_link = software_link
        self.specifications_link = specifications_link
        self.maintenance_link = maintenance_link

    def set_software_link(self, driver):
        self.software_link = Software_and_Drivers_Link(driver)

    def set_specifications_link(self, driver, identifier):
        self.specifications_link = Product_Specifications_Link(driver, identifier)

    def set_maintenance_link(self, driver):
        self.maintenance_link = Maintenance_and_Service_Guide_Link(driver)

    def get_software_link(self):
        return self.software_link

    def get_specifications_link(self):
        return self.specifications_link

    def get_maintenance_link(self):
        return self.maintenance_link

    def get_full_product_name(self):
        return self.full_product_name

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
Device = {}

# Signs into the support community
Sign_In_Notifications(driver)

Main_Product_Page_Close(driver)

# Finds unread mentions
notification_list = driver.find_element_by_id("notificationList")
ul = notification_list.find_element_by_xpath(".//ul")

while True:
    unread_mention_list = ul.find_elements_by_xpath(".//li[@class='lia-notification-feed-item lia-notification-mentions lia-component-notificationfeed-widget-notification-feed-item']") #lia-notification-feed-item lia-notification-mentions lia-notification-unread lia-component-notificationfeed-widget-notification-feed-item

    if (len(unread_mention_list) == 0):
        driver.refresh()
    else:
        # Loops through unread mentions
        for mention in unread_mention_list:
            user_element = mention.find_element_by_xpath(".//div/div/div[2]/div/span")
            driver.execute_script("arguments[0].scrollIntoView();", user_element)
            user_text = user_element.text

            # Checks if the user is EddyK
            if user_text == 'EddyK': 
                final_answer = ""

                # Opens forum thread with unread mention in new tab
                forum_thread_link = mention.find_element_by_xpath(".//div/div/div[2]/div/a")
                forum_thread_link.send_keys(Keys.CONTROL + Keys.ENTER)
                driver.switch_to.window(driver.window_handles[1])

                # Returns the country of the original poster, if available, and clicks on 'Reply' of the post containing the unread mention
                country = Identify_Post_and_Country(driver)

                # Returns the full command and identifies the individual commands from the mention
                full_command = Return_Commands(driver)
                individual_commands = full_command.split(",")

                # Checks if the command is only a support command
                if (len(full_command.split(" ")) == 1):
                    # Support Function Only
                    pass
                else:
                    # Finds the identifier in the full command
                    i = full_command.split(",")
                    for j in i:
                        k = j.split(" ")
                        if Command_Type(k[1]) == 1:
                            identifier = " ".join(k[2:])
                            break

                    # Opens the main product page in browser handle 2 and returns the full product name 
                    full_product_name, final_answer = Main_Product_Page(driver, identifier, final_answer)

                    # Checks if the full product name exists in the MySQL database
                    if Check_If_Exist(mycursor, full_product_name):
                        # Retrieves all links from the SQL database
                        software_link, specifications_link, maintenance_link = SQL_Get_Links(mycursor, full_product_name)
                        #
                        Device[identifier] = Product(driver, full_product_name, final_answer, software_link, specifications_link, maintenance_link)

                        # SQL COMMAND SWITCHER
                        for individual_command in individual_commands:
                            split_individual_command = individual_command.split(" ")
                            command_number = Command_Type(split_individual_command[1])
                            # Specifications
                            if command_number == 2:
                                Device[identifier].set_specifications_link(driver, identifier)
                                if Device[identifier].get_specifications_link == None:
                                    Device[identifier].final_answer += '<p>Product Specifications for the %s were not found.<p>' % Device[identifier].get_full_product_name()
                                else: 
                                    Open_URL(driver, Device[identifier].get_specifications_link)
                                    if len(split_individual_command) == 2:
                                        Product_Specifications_Answer(driver, Device[identifier], "all", Device[identifier].get_specifications_link(), Device[identifier].get_full_product_name)
                                    else:
                                        Product_Specifications_Answer(driver, Device[identifier], split_individual_command[2:], Device[identifier].get_specifications_link(), Device[identifier].get_full_product_name)
                            # Maintenance
                            elif command_number == 3:
                                Device[identifier].set_maintenance_link(driver)
                                if Device[identifier].get_maintenance_link == None:
                                    Device[identifier].final_answer += '<p>The Maintenance and Service Guide for the %s was not found.<p>' % Device[identifier].get_full_product_name()
                                else: 
                                    Open_URL(driver, Device[identifier].get_maintenance_link)
                                    if command_number == 3:
                                        if len(split_individual_command) == 2:
                                            Maintenance_and_Service_Guide_Answer(driver, Device[identifier], "No Page", Device[identifier].get_maintenance_link(), Device[identifier].get_full_product_name)
                                        else:
                                            Maintenance_and_Service_Guide_Answer(driver, Device[identifier], split_individual_command[2], Device[identifier].get_maintenance_link(), Device[identifier].get_full_product_name)
                            # Software
                            elif command_number == 4:
                                Device[identifier].set_software_link(driver)
                                if Device[identifier].get_maintenance_link == None:
                                    Device[identifier].final_answer += '<p>The Software and Drivers page for the %s was not found.<p>' % Device[identifier].get_full_product_name()
                                else: 
                                    Open_URL(driver, Device[identifier].get_software_link)
                                    Software_and_Drivers_Answer(driver, Device[identifier], split_individual_command[2:], Device[identifier].get_software_link(), Device[identifier].get_full_product_name)
                            elif command_number == 5:
                                # Support
                                pass
                            else:
                                Device[identifier].final_answer += "<p>The command '<i>%s</i>' was not recognized.</p>" % (split_individual_command[1])

                        driver.get("https://support.hp.com/us-en/products")
                    else:
                        # Creates new product instance and assigns it to the dictionary device, which is accessible through the identifier
                        Device[identifier] = Product(driver, full_product_name, final_answer, "", "", "")

                        specifications_request_is_found = False
                        maintenance_request_is_found = False
                        software_request_is_found = False

                        # SELENIUM COMMAND SWITCHER
                        for individual_command in individual_commands:
                            split_individual_command = individual_command.split(" ")
                            command_number = Command_Type(split_individual_command[1])
                            # Specifications
                            if command_number == 2:
                                specifications_request_is_found = True
                                if len(split_individual_command) == 2:
                                    specs_arguments = "all"
                                else:
                                    specs_arguments = split_individual_command[2:]
                            # Maintenance
                            elif command_number == 3:
                                maintenance_request_is_found = True
                                if command_number == 3:
                                    if len(split_individual_command) == 2:
                                        maintenance_argument = "No Page"
                                    else:
                                        maintenance_argument = split_individual_command[2]
                            # Software
                            elif command_number == 4:
                                software_request_is_found = True
                                software_arguments = split_individual_command[2:]
                            elif command_number == 5:
                                # Support
                                pass
                            else:
                                Device[identifier].final_answer += "<p>The command '<i>%s</i>' was not recognized.</p>" % (split_individual_command[1])

                        # Opens the Specifications page, saves it, and leaves the tab open
                        Device[identifier].set_specifications_link(driver, identifier)
                        if specifications_request_is_found:
                            Product_Specifications_Answer(driver, Device[identifier], specs_arguments, Device[identifier].get_specifications_link(), Device[identifier].get_full_product_name)
                        # Closes New Tab
                        Close_Current_Tab(driver)

                        # Opens the Maintenance and Service Guide page, saves it, and leaves the tab open
                        Device[identifier].set_maintenance_link(driver)
                        if maintenance_request_is_found:
                            Maintenance_and_Service_Guide_Answer(driver, Device[identifier], maintenance_argument, Device[identifier].get_maintenance_link(), Device[identifier].get_full_product_name)
                        # Closes New Tab
                        Close_Current_Tab(driver)

                        # Opens the Software and Drivers page in the same tab, saves it, and reverts it back to the default main product page
                        Device[identifier].set_software_link(driver)
                        if software_request_is_found:
                            Software_and_Drivers_Answer(driver, Device[identifier], software_arguments, Device[identifier].get_software_link(), Device[identifier].get_full_product_name)
                        
                        driver.get("https://support.hp.com/us-en/products")

                        SQL_Store_Links(mycursor, db, Device[identifier].get_full_product_name(), Device[identifier].get_software_link(), Device[identifier].get_specifications_link(), Device[identifier].get_maintenance_link())

                driver.switch_to.window(driver.window_handles[1])
                Input_Submit(driver, Device[identifier])
                #driver.close()
                #driver.switch_to.window(driver.window_handles[0])