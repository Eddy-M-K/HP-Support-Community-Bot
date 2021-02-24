from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.common.exceptions import NoSuchElementException

model_name = "ap0053dx"
softpaq_names = ["sp100917.exe", "sp96876.exe"]

answer = '<hr /><p><font size="5"><strong>Software and Drivers</strong></font></p><p>&nbsp;</p>'

driver = webdriver.Edge(r"C:\Users\EddyM\Downloads\edgedriver_win64 (1)\msedgedriver.exe")

driver.get('https://support.hp.com/us-en/products')

driver.implicitly_wait(10)
accept = driver.find_element_by_id('onetrust-accept-btn-handler')
accept.click()

search_box = driver.find_element_by_id('search-input-pfinder')
search_box.send_keys(model_name)

find_button = driver.find_element_by_id('btnSplitSearchSubmit')
find_button.click()

driver.implicitly_wait(10)
full_product_name = driver.find_element_by_xpath("//div[@id='pdpPrdctHeading']/h2").text

x_button = driver.find_element_by_id("dismiss-notifications")
x_button.click()

software_button = driver.find_element_by_id("drivers")
driver.execute_script("arguments[0].scrollIntoView();", software_button)
driver.execute_script("arguments[0].click();", software_button)

driver.implicitly_wait(10)
open_all = driver.find_element_by_id("open-close-toggle-tag")
open_all.click()

for softpaq_name in softpaq_names:
    softpaq = driver.find_element_by_xpath(".//*[@title='%s']" % softpaq_name)
    softpaq_link = softpaq.get_attribute('href')
    tbody = softpaq.find_element_by_xpath(".//../../../../../../..")
    driver_title = tbody.find_element_by_class_name("driverTitleRTL")
    driver.execute_script("arguments[0].scrollIntoView();", driver_title)
    driver.execute_script("arguments[0].click();", driver_title)
    driver_name = driver_title.find_element_by_xpath(".//p").text

    left_section_parent = softpaq.find_element_by_xpath(".//../../..")
    left_section_content = []
    for x in range(5):
        left_section_content.append(left_section_parent.find_element_by_xpath(".//div[%d]/*[2]" % (x + 1)).text)

    both_section_parent = left_section_parent.find_element_by_xpath(".//..")
    dividers = both_section_parent.find_elements_by_xpath(".//div")
    description = dividers[8].find_element_by_xpath(".//p[2]").text

    fix = dividers[10].text
    if len(fix) > 0:
        fix_is_found = True
    else: 
        fix_is_found = False

    answer += """
    <p><strong>%s</strong></p>
    <p><strong><a href="%s" target="_self">Download</a></strong></p>
    <table border="1">
    <tbody>
    <tr>
    <td><strong>Type:</strong></td>
    <td><span>%s</span></td>
    </tr>
    <tr>
    <td><strong>Version:</strong></td>
    <td>%s</td>
    </tr>
    <tr>
    <td><strong>Operating System:</strong></td>
    <td>%s</td>
    </tr>
    <tr>
    <td><strong>Release Date:</strong></td>
    <td>%s</td>
    </tr>
    <tr>
    <td><strong>File Name and Size:</strong></td>
    <td>%s</td>
    </tr>
    <tr>
    <td><strong>Description:</strong></td>
    <td><span>%s</span></td>
    </tr>
    """ % (driver_name, softpaq_link, left_section_content[0], left_section_content[1], left_section_content[2], left_section_content[3], left_section_content[4], description)

    if fix_is_found:
        answer += "<tr><td><strong>Fixes and Enhancements:</strong></td><td><span>%s</span></td></tr>" % (fix)

    answer += '</tbody></table><p class="lia-align-right">&nbsp;</p>'

answer += """
<p class="lia-align-center"><span>By downloading, you agree to HP's terms and conditions.&nbsp;</span><a href="https://support.hp.com/us-en/document/c00581401" target="_blank" rel="noopener">HP Software License Agreement.</a></p>
"""