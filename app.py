from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Firefox()

"""
    - The function below, when called, opens up the browser and goes to wwww.pakwheels.com and then navigates to their
      used cars section.
      
    - It then inserts queries into their query bar such as:
      Car Make Model
      City
      Price Range
      From - To Year
      
    - Finally it clicks on the search button and the page with the inserted criteria opens 
"""


def navigate_links():
    driver.get("https://www.pakwheels.com")
    time.sleep(2)
    driver.find_element_by_id('onesignal-popover-cancel-button').click()
    time.sleep(5)
    driver.find_element_by_link_text('Used Cars').click()
    driver.find_element_by_id('more_option').click()
    driver.find_element_by_name('home-query').send_keys('Honda Civic')
    driver.find_element_by_class_name('chzn-single').click()
    driver.find_element_by_id('UsedCity_chzn_o_4').click()
    pr_range = driver.find_element_by_id('pr-range-filter')
    pr_range.click()
    driver.find_element_by_id('pr_from').send_keys('10')
    driver.find_element_by_id('pr_to').send_keys('18')
    pr_range.click()
    yr_from = Select(driver.find_element_by_id('YearFrom'))
    yr_to = Select(driver.find_element_by_id('YearTo'))
    yr_from.select_by_value('2008')
    yr_to.select_by_value('2012')
    driver.find_element_by_id('used-cars-search-btn').click()



try:
    print('initialized headless')
    navigate_links()
finally:
    # driver.quit()
    print("done")
