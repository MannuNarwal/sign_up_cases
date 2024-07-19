import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from helpersF import getUrlDriver

@pytest.fixture()
def all_variable_needed():
    driver = getUrlDriver('https://zouk.co.in')
    yield {
        "driver": driver,
        "opened_url": ""
    }
    driver.quit()