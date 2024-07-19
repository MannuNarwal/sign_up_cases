from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def getUrlDriver(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver

def click_button(driver, by, xpath):
    try:
        button = driver.find_element(by, xpath)
        button.click()
        sleep(1)
    except Exception as e:
        print(f"An error occurred while clicking button: {e}")

def enter_text(driver, by, xpath, text):
    try:
        element = driver.find_element(by, xpath)
        element.send_keys(text)
        sleep(1)
    except Exception as e:
        print(f"An error occurred while entering text: {e}")

def get_element_text(driver, by, xpath):
    try:
        element = driver.find_element(by,xpath)
        return element.text
    except Exception as e:
        print(f"An error occurred while getting element text: {e}")
        return ""

def assert_verification(actual_value, expected_value, msg):
    assert actual_value == expected_value, msg

def assert_url(driver, expected_url, msg):
    try:
        current_url = driver.current_url
        assert current_url == expected_url, msg
    except Exception as e:
        print(f"An error occurred while asserting URL: {e}")

def clear_text(driver, by, xpath):
    try:
        element = driver.find_element(by, xpath)
        element.clear()
        sleep(1)
    except Exception as e:
        print(f"An error occurred while clearing text: {e}")

def wait_for_element(driver, by, xpath, timeout=10):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, xpath)))
        return element
    except Exception as e:
        print(f"An error occurred while waiting for element: {e}")
        return None
