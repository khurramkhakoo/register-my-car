from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from constants import URL
from util import *

# Path to your ChromeDriver
chrome_driver_path = '/usr/local/bin/chromedriver'  # Update this path to where your ChromeDriver is located

# Initialize WebDriver
service: Service = Service(chrome_driver_path)
driver: webdriver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get(URL)
time.sleep(3)


click_register_button(driver)
fill_property_name_form(driver)
select_property(driver)
choose_visitor_parking(driver)
add_vehicle_information(driver)


# Closing the browser
driver.quit()
