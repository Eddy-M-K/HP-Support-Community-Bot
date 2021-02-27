def Close_Tab(driver):
    driver.close()
    driver.switch_to.window(driver.window_handles[2])