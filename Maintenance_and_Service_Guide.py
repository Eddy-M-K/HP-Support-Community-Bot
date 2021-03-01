from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 
from selenium.common.exceptions import NoSuchElementException

def Maintenance_and_Service_Guide_Link(driver):
    manuals = driver.find_element_by_id('manuals')
    manuals.click()

    try:
        maintenance_and_service_guide_text = driver.find_element_by_xpath("//tbody[@id='userGuidesList']/tr/td/a/*[contains(text(), 'Maintenance and Service Guide')]")
        driver.execute_script("arguments[0].scrollIntoView();", maintenance_and_service_guide_text)
        driver.execute_script("arguments[0].click();", maintenance_and_service_guide_text)
        maintenance_and_service_guide_page = maintenance_and_service_guide_text.find_element_by_xpath('..').get_attribute('href')
        driver.switch_to.window(driver.window_handles[3])

        return maintenance_and_service_guide_page
    except NoSuchElementException:
        return None

def Maintenance_and_Service_Guide_Answer(driver, device, page, url, full_product_name):
    device.final_answer += '<hr /><p><font size="5"><strong>Maintenance and Service Guide</strong></font></p>'
    if page == "No Page":
        device.final_answer += '<p><strong><a href="%s" target="_blank" rel="noopener">Maintenance and Service Guide</a> for the %s.</strong></p><p>&nbsp;</p>' % (url, full_product_name)
        device.final_answer += '''<p>By choosing to use the Maintenance and Service Guide to make hardware changes to the device, 
                                    the user understands that HP is not liable for any accidental damage inflicted upon the device 
                                    and that modifications are not covered under HP's standard warranty. For additional protection 
                                    in the case of accidental damage, refer to HP's ADP plans for your product.</p><p>&nbsp;</p>
                                    <p class="lia-align-center">Full details on <a href="https://www8.hp.com/us/en/privacy/limited_warranty.html" 
                                    target="_blank" rel="noopener">HP's Worldwide Limited Warranty and Technical Support</a>.</p>
                                    <p class="lia-align-center">Full details on <a href="https://support.hp.com/ca-en/document/c05805564" 
                                    target="_blank" rel="noopener">Damage Not Covered by the HP Standard Limited Warranty</a>.</p>'''

        return
    else:
        url += "#page=%s" % page
        device.final_answer += '<p><strong>Page %s of the <a href="%s" target="_blank" rel="noopener">Maintenance and Service Guide</a> for the %s.</strong></p><p>&nbsp;</p>' % (page, url, full_product_name)

    device.final_answer += '''<p>By choosing to use the Maintenance and Service Guide to make hardware changes to the device, 
                                the user understands that HP is not liable for any accidental damage inflicted upon the device 
                                and that modifications are not covered under HP's standard warranty. For additional protection 
                                in the case of accidental damage, refer to HP's ADP plans for your product.</p><p>&nbsp;</p>
                                <p class="lia-align-center">Full details on <a href="https://www8.hp.com/us/en/privacy/limited_warranty.html" 
                                target="_blank" rel="noopener">HP's Worldwide Limited Warranty and Technical Support</a>.</p><p>&nbsp;</p>
                                <p class="lia-align-center">Full details on <a href="https://support.hp.com/ca-en/document/c05805564" 
                                target="_blank" rel="noopener">Damage Not Covered by the HP Standard Limited Warranty</a>.</p>'''

    return