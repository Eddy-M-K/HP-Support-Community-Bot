from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.common.exceptions import NoSuchElementException
import mysql.connector

support_options = mysql.connector.connect(
    host = "localhost",
    user = "",
    password = ""
)

support_options_cursor = support_options.cursor()

support_options_cursor.execute("CREATE DATABASE ")