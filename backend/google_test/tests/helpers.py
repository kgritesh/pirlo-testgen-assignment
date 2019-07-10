from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def until_url_changed(driver, max_wait):
    WebDriverWait(driver, max_wait).until(EC.url_changes(driver.current_url))
