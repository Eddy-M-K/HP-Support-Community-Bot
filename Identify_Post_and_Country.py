from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import NoSuchElementException


# Identifies the correct post within the thread to reply to
# With HP Expert mode enabled, also finds the country of the original poster

def Identify_Post_and_Country(driver):
    original_post = driver.find_element_by_class_name("first-message")
    driver.execute_script("arguments[0].scrollIntoView();", original_post)

    try:
        country_element = original_post.find_element_by_class_name("user-location-wrap")
        country = country_element.text
    except NoSuchElementException:
        # If the country tag is not found, defaults to Worldwide
        country = "Worldwide"

    post_url = driver.current_url
    split_url = post_url.split("/")

    for url in split_url:
        if '#' in url:
            string_hash = url.split("#")
            # Finds the post number from the URL
            post_number = string_hash[0]
            break

    post = driver.find_element_by_xpath("//div[@data-lia-message-uid='%s']" % post_number)
    driver.execute_script("arguments[0].scrollIntoView();", post)
    reply_button = post.find_element_by_xpath(".//a[@class='lia-button lia-button-secondary reply-action-link lia-action-reply']")
    driver.execute_script("arguments[0].scrollIntoView();", reply_button)
    driver.execute_script("arguments[0].click();", reply_button)

    return country