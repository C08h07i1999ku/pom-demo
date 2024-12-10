import pytest
from selenium import webdriver
from urllib3 import request


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver




