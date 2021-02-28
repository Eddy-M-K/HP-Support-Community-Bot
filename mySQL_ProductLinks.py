from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 
from selenium.common.exceptions import NoSuchElementException
import mysql.connector

def Check_If_Exist(mycursor, full_product_name):
    #mycursor.execute("CREATE DATABASE HP")
    #mycursor.execute("CREATE TABLE ProductLinks (full_product_name VARCHAR(100) PRIMARY KEY, software_link VARCHAR(255), specifications_link VARCHAR(255), maintenance_link VARCHAR(255))")
    '''
    mycursor.execute("DESCRIBE ProductLinks")

    for x in mycursor:
        print(x)
    '''
    '''
    sql = "INSERT INTO ProductLinks (full_product_name, software_link, specifications_link, maintenance_link) VALUES (%s, %s, %s, %s)"
    val = (full_product_name, None, None, None)
    mycursor.execute(sql, val)
    db.commit()
    '''
    mycursor.execute("SELECT * FROM ProductLinks WHERE full_product_name = %s GROUP BY full_product_name", (full_product_name,))
    
    results = mycursor.fetchall()
    rowcount = mycursor.rowcount

    if rowcount:
        return True
    else:
        return False

def SQL_Get_Links(mycursor, full_product_name):
    mycursor.execute("SELECT software_link, specifications_link, maintenance_link From ProductLinks WHERE full_product_name = %s", (full_product_name,))
    result = (mycursor.fetchall()[0])
   
    return result[0], result[1], result[2]

    '''
    for value in result:
        print("%s" % value[0])
        print("%s" % value[1])
        print("%s" % value[2])
    '''

def SQL_Link_Open(driver, url):
    driver.get('%s' % url)