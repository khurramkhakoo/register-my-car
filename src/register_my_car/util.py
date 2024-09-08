import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from constants import *

def click_register_button(driver: webdriver) -> None:
    try:
        # Locate the button by its text
        register_button = driver.find_element(By.LINK_TEXT, 'Register Vehicle')
        register_button.click()
        print("Button clicked successfully!")

        # Wait for the next page to load
        time.sleep(3)
    except Exception as e:
        print(f"Error clicking the button: {e}")
        driver.quit()


def fill_property_name_form(driver: webdriver) -> None:
    try:
        # Locate the form field by its id
        property_field = driver.find_element(By.ID, 'propertyName')
        property_field.send_keys('Capitol')
        print("Property name added")

        time.sleep(3)

        confirm_button = driver.find_element(By.ID, 'confirmProperty')
        confirm_button.click()
        print("Confirm button clicked successfully")

        time.sleep(3)
    except Exception as e:
        print(f"Error adding property name: {e}")
        driver.quit()


def select_property(driver: webdriver) -> None:
    try:
        select_button = driver.find_element(By.CLASS_NAME, 'select-property')
        select_button.click()
        print("Select button clicked successfully")

        time.sleep(3)
    except Exception as e:
        print(f"Error: {e}")
        driver.quit()


def choose_visitor_parking(driver: webdriver) -> None:
    try:
        parking_button = driver.find_element(By.ID, 'registrationTypeVisitor')
        parking_button.click()
        print("Parking button clicked successfully")

        time.sleep(3)
    except Exception as e:
        print(f"Error: {e}")
        driver.quit()


def add_vehicle_information(driver: webdriver) -> None:
    try:
        apartment_number_field = driver.find_element(By.ID, 'vehicleApt')
        apartment_number_field.send_keys(os.environ.get('VEHICLE_APT'))
        time.sleep(1)

        apartment_number_field = driver.find_element(By.ID, 'vehicleMake')
        apartment_number_field.send_keys(VEHICLE_MAKE)
        time.sleep(1)

        apartment_number_field = driver.find_element(By.ID, 'vehicleModel')
        apartment_number_field.send_keys(VEHICLE_MODEL)
        time.sleep(1)

        apartment_number_field = driver.find_element(By.ID, 'vehicleLicensePlate')
        apartment_number_field.send_keys(VEHICLE_LICENSE_PLATE)
        time.sleep(1)

        apartment_number_field = driver.find_element(By.ID, 'vehicleLicensePlateConfirm')
        apartment_number_field.send_keys(VEHICLE_LICENSE_PLATE)

        print("Form filled successfully")

        time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
        driver.quit()


def take_screenshot(driver: webdriver) -> None:
    try:
        driver.save_screenshot('ss.png')
        print("Successfully saved screenshot to ss.png")

        time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
        driver.quit()
