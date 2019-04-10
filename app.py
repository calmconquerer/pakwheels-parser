from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import csv
import bs4 as bs


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


def navigation():
    driver.get("https://www.pakwheels.com")
    WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.ID, 'onesignal-popover-cancel-button')))
    driver.find_element_by_id('onesignal-popover-cancel-button').click()
    time.sleep(3)
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


'''

    - This function gets all the required links.
    
    - Firstly it gets all the Anchor tags that has the required links (class = "car-name ad-detail-path")
    
    - Then through the for-loop, it further parses the anchor tags to get the href from the anchor tags one by one and appends it to another list called as links and returns that list.
    

'''


def get_car_links():
    navigation()
    links = []
    elems = driver.find_elements(By.XPATH, '//a[@class = "car-name ad-detail-path"]')
    for elem in elems:
        links.append(elem.get_attribute('href'))
    return links


try:
    print('Starting')
    get_car_links()
finally:
    print('Done')
    driver.quit()
