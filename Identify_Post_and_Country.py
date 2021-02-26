def Identify_Post_and_Country(driver):
    x_button = driver.find_element_by_class_name("close")
    x_button.click()

    original_post = driver.find_element_by_class_name("first-message")
    driver.execute_script("arguments[0].scrollIntoView();", original_post)

    try:
        country = original_post.find_element_by_class_name("user-location-wrap").text
    except NoSuchElementException:
        country = "Worldwide"

    post_url = driver.current_url
    split_url = post_url.split("/")

    for url in split_url:
        if (url.isdigit()):
            post_number = url
            break 

    post = driver.find_element_by_xpath("//div[@data-lia-message-uid='%s']" % post_number) #get number from end of url
    driver.execute_script("arguments[0].scrollIntoView();", post)

    reply = post.find_element_by_xpath(".//a[@class='lia-button lia-button-secondary reply-action-link lia-action-reply']")
    driver.execute_script("arguments[0].scrollIntoView();", reply)
    driver.execute_script("arguments[0].click();", reply)

    return country