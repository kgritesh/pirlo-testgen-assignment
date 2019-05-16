from selenium import webdriver

import pytest


@pytest.fixture()
def chrome_driver():
    return webdriver.Chrome()


