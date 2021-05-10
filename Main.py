from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import mysql.connector
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

# Product Class Definition
class Product:
    def __init__(self, driver, full_product_name, final_answer, software_link, specifications_link, maintenance_link):
        self.full_product_name = full_product_name
        self.final_answer = final_answer
        self.software_link = software_link
        self.specifications_link = specifications_link
        self.maintenance_link = maintenance_link

    # --- Default setters ---

    def set_software_link(self, url):
        self.software_link = url

    def set_specifications_link(self, url):
        self.specifications_link = url

    def set_maintenance_link(self, url):
        self.maintenance_link = url

    # --- Default setters End ---

    # --- Methods to retrieve URLs ---

    def find_software_link(self, driver):
        return Software_and_Drivers_Link(driver)

    def find_specifications_link(self, driver, identifier):
        return Product_Specifications_Link(driver, identifier)

    def find_maintenance_link(self, driver):
        return Maintenance_and_Service_Guide_Link(driver)

    # --- URL Retrieval Methods End ---

    # --- Default getters ---

    def get_software_link(self):
        return self.software_link

    def get_specifications_link(self):
        return self.specifications_link

    def get_maintenance_link(self):
        return self.maintenance_link

    def get_full_product_name(self):
        return self.full_product_name

    # --- Default getters End ---

# --- SQL Sign In and cursor object creation for a SQL database located on the local host ---

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

# --- Local Host SQL DB End ---

# --- SQL Sign In and cursor object creation for a SQL database located on Microsoft Azure ---
'''
s = open("azure_mysql_signin.txt", "r")
server = s.readline()
user = s.readline()
password = s.readline()

db = mysql.connector.connect(
    host = "%s" % server,
    user = "%s" % user,
    password = "%s" % password,
    database = "HP"
)

mycursor = db.cursor()
'''
# --- MS Azure SQL DB End ---

# --- Driver Creation ---

# driver = webdriver.Edge(r"C:\Users\EddyM\Downloads\edgedriver_win64 (1)\msedgedriver.exe")
driver = webdriver.Chrome(r"C:\Users\EddyM\Downloads\chromedriver_win32\chromedriver.exe")
driver.get('https://h30434.www3.hp.com/t5/notificationfeed/page')
driver.maximize_window()

# --- Driver Creation End ---

# Declares the Product dictionary, which will act as a list of instances of the "Product" class
Device = {}

# Signs into the support community
Sign_In_Notifications(driver)

# Opens HP Support's Main Support Page to close intrusive popups once
Main_Product_Page_Close(driver)

while True:
    # Identifies notification list
    notification_list = driver.find_element_by_id("notificationList")
    ul = notification_list.find_element_by_xpath(".//ul")

    # Finds unread mentions
    driver.implicitly_wait(5)
    unread_mention_list = ul.find_elements_by_xpath(".//li[@class='lia-notification-feed-item lia-notification-mentions lia-notification-unread lia-component-notificationfeed-widget-notification-feed-item']") #lia-notification-feed-item lia-notification-mentions lia-component-notificationfeed-widget-notification-feed-item

    if (len(unread_mention_list) == 0):
        pass
    else:
        # Loops through unread mentions
        for mention in unread_mention_list:
            user_element = mention.find_element_by_xpath(".//div/div/div[2]/div/span")
            driver.execute_script("arguments[0].scrollIntoView();", user_element)
            user_text = user_element.text

            # Checks if the user mentioning the bot is EddyK
            if user_text == 'EddyK': 
                # Initializes the final answer
                final_answer = ""

                # Opens forum thread with the unread mention in a new tab
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

                    # Opens the Main Product Page in browser handle 2 and returns the full product name 
                    full_product_name, final_answer = Main_Product_Page(driver, identifier, final_answer)

                    # Checks if the full product name exists in the MySQL database
                    if Check_If_Exist(mycursor, full_product_name):
                        # Retrieves all links from the SQL database
                        software_link, specifications_link, maintenance_link = SQL_Get_Links(mycursor, full_product_name)

                        Device[identifier] = Product(driver, full_product_name, final_answer, software_link, specifications_link, maintenance_link)

                        # SQL Database Command Switcher 
                        for individual_command in individual_commands:
                            split_individual_command = individual_command.split(" ")
                            command_number = Command_Type(split_individual_command[1])
                            # Pass the 'product' command
                            if command_number == 1:
                                pass
                            # Specifications
                            elif command_number == 2:
                                if Device[identifier].get_specifications_link == None:
                                    Device[identifier].final_answer += '<p>Product Specifications for the %s were not found.<p>' % Device[identifier].get_full_product_name()
                                else: 
                                    Open_URL(driver, Device[identifier].get_specifications_link())
                                    if len(split_individual_command) == 2:
                                        Product_Specifications_Answer(driver, Device[identifier], "all", Device[identifier].get_specifications_link(), Device[identifier].get_full_product_name())
                                    else:
                                        Product_Specifications_Answer(driver, Device[identifier], split_individual_command[2:], Device[identifier].get_specifications_link(), Device[identifier].get_full_product_name())
                            # Maintenance
                            elif command_number == 3:
                                if Device[identifier].get_maintenance_link == None:
                                    Device[identifier].final_answer += '<p>The Maintenance and Service Guide for the %s was not found.<p>' % Device[identifier].get_full_product_name()
                                else: 
                                    if command_number == 3:
                                        if len(split_individual_command) == 2:
                                            Maintenance_and_Service_Guide_Answer(driver, Device[identifier], "No Page", Device[identifier].get_maintenance_link(), Device[identifier].get_full_product_name())
                                        else:
                                            Maintenance_and_Service_Guide_Answer(driver, Device[identifier], split_individual_command[2], Device[identifier].get_maintenance_link(), Device[identifier].get_full_product_name())
                            # Software
                            elif command_number == 4:
                                if Device[identifier].get_maintenance_link == None:
                                    Device[identifier].final_answer += '<p>The Software and Drivers page for the %s was not found.<p>' % Device[identifier].get_full_product_name()
                                else: 
                                    Open_URL(driver, Device[identifier].get_software_link())
                                    Software_and_Drivers_Answer(driver, Device[identifier], split_individual_command[2:], Device[identifier].get_software_link(), Device[identifier].get_full_product_name())
                            elif command_number == 5:
                                # Support
                                pass
                            else:
                                Device[identifier].final_answer += "<p>The command '<i>%s</i>' was not recognized.</p>" % (split_individual_command[1])
                    else:
                        # Creates new product instance and assigns it to the dictionary device, which is accessible through the identifier
                        Device[identifier] = Product(driver, full_product_name, final_answer, "", "", "")

                        specifications_request_is_found = False
                        maintenance_request_is_found = False
                        software_request_is_found = False

                        # Selenium Command Switcher
                        for individual_command in individual_commands:
                            split_individual_command = individual_command.split(" ")
                            command_number = Command_Type(split_individual_command[1])
                            # Pass the 'product' command
                            if command_number == 1:
                                pass
                            # Specifications
                            elif command_number == 2:
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
                        Device[identifier].set_specifications_link(Device[identifier].find_specifications_link(driver, identifier))
                        if specifications_request_is_found:
                            if Device[identifier].get_specifications_link == None:
                                    Device[identifier].final_answer += '<p>Product Specifications for the %s were not found.<p>' % Device[identifier].get_full_product_name()
                            else:
                                Product_Specifications_Answer(driver, Device[identifier], specs_arguments, Device[identifier].get_specifications_link(), Device[identifier].get_full_product_name())
                        # Closes New Tab
                        Close_Current_Tab(driver)

                        # Opens the Maintenance and Service Guide page, saves it, and leaves the tab open
                        Device[identifier].set_maintenance_link(Device[identifier].find_maintenance_link(driver))
                        if maintenance_request_is_found:
                            if Device[identifier].get_maintenance_link == None:
                                Device[identifier].final_answer += '<p>The Maintenance and Service Guide for the %s was not found.<p>' % Device[identifier].get_full_product_name()
                            else:
                                Maintenance_and_Service_Guide_Answer(driver, Device[identifier], maintenance_argument, Device[identifier].get_maintenance_link(), Device[identifier].get_full_product_name())
                        # Closes New Tab
                        Close_Current_Tab(driver)

                        # Opens the Software and Drivers page in the same tab, saves it, and reverts it back to the default main product page
                        Device[identifier].set_software_link(Device[identifier].find_software_link(driver))
                        if software_request_is_found:
                            if Device[identifier].get_maintenance_link == None:
                                Device[identifier].final_answer += '<p>The Software and Drivers page for the %s was not found.<p>' % Device[identifier].get_full_product_name()
                            else: 
                                Software_and_Drivers_Answer(driver, Device[identifier], software_arguments, Device[identifier].get_software_link(), Device[identifier].get_full_product_name())

                        SQL_Store_Links(mycursor, db, Device[identifier].get_full_product_name(), Device[identifier].get_software_link(), Device[identifier].get_specifications_link(), Device[identifier].get_maintenance_link())

                driver.close()
                driver.switch_to.window(driver.window_handles[1])
                # Submit the answer
                Input_Submit(driver, Device[identifier])

                driver.close()
                # Reset to first browser handle
                driver.switch_to.window(driver.window_handles[0])

    # Refresh the notifications page to check for new notifications
    driver.refresh()