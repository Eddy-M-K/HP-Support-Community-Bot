def Return_Commands(driver):
    driver.implicitly_wait(10)
    post_box = driver.find_element_by_id("bodyDisplay")
    mention = post_box.find_element_by_xpath(".//a[@href='/t5/user/viewprofilepage/user-id/3211563']")
    driver.execute_script("arguments[0].scrollIntoView();", mention)
    text = mention.find_element_by_xpath(".//..").text

    full_command = text.removeprefix('@SpectreFolio')

    return full_command