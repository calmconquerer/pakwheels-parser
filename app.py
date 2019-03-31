from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()


def navigate_links():
    driver.get("https://www.pakwheels.com")
    driver.find_element_by_id('onesignal-popover-cancel-button').click()
    time.sleep(5)
    driver.find_element_by_link_text('Used Cars').click()
    driver.find_element_by_id('more_option').click()
    driver.find_element_by_name('home-query').send_keys('Honda Civic')


try:
    print('initialized headless')
    navigate_links()
finally:
    # driver.quit()
    print("done")
