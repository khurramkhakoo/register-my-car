from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from constants import URL
from util import *

app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])
def your_function():
    # Path to your ChromeDriver
    chrome_driver_path = '/usr/bin/chromedriver'
    service: Service = Service(chrome_driver_path)

    # Adding headless options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1400,1500")

    # Initialize WebDriver
    driver: webdriver = webdriver.Chrome(service=service, options=options)

    # Navigate to the website
    driver.get(URL)
    time.sleep(3)

    click_register_button(driver)
    fill_property_name_form(driver)
    select_property(driver)
    choose_visitor_parking(driver)
    add_vehicle_information(driver)
    # submit_final_form(driver)
    take_screenshot(driver)
    upload_screenshot_to_s3(driver)

    # Closing the browser
    driver.quit()

    return jsonify({"message": "API is working!"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
