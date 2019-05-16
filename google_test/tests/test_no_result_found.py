import tests.helpers
from selenium.webdriver.remote.webelement import WebElement


test_config = {
    "step_wait": 10,
    "base_url": "https://google.com",
    "description": "Search for random query and assert that nothing is found on google",
    "steps": [
        {"step_wait": 0},
        {"step_wait": 0},
        {"step_wait": 0},
        {"step_wait": 0},
        {"step_wait": 0},
    ],
}


def step_1(chrome_driver):
    """
    Enter Text
    """
    try:
        elem = chrome_driver.find_element_by_name("q")
    except Exception as ex:
        print(ex)
        elem = None

    if not elem:
        raise Exception("Test Failed at step 1")

    elem.send_keys("dbmndbndbndjkbdkbdgbdgbdgbgdkbkgk")
    chrome_driver.implicitly_wait(0)


def step_2(chrome_driver):
    """
    Click Search Button
    """
    try:
        elems = chrome_driver.find_elements_by_css_selector("center > input")
        position = 2
        elem = elems[position] if len(elems) >= position else None
    except Exception as ex:
        elem = None

    if not elem:
        try:
            elem = chrome_driver.find_element_by_css_selector(
                "input[value='Google Search']"
            )
        except Exception as ex:
            print(ex)
            elem = None

    if not elem:
        raise Exception("Test Failed at Step 2")

    elem_type = elem.get_attribute("type")
    if elem_type == "submit":
        elem.submit()
    else:
        elem.click()
    chrome_driver.implicitly_wait(0)


def step_3(chrome_driver):
    """
    Wait for 10 seconds
    """
    helpers.until_url_changed(chrome_driver, 30)
    chrome_driver.implicitly_wait(0)


def step_4(chrome_driver):
    try:
        elem = chrome_driver.find_element_by_xpath("//div[@id='topstuff']/div/div/p")
    except Exception:
        elem = None

    if not elem:
        raise Exception("Test Failed at step 4")

    assert elem.text.contains(
        "Your search - dbmndbndbndjkbdkbdgbdgbdgbgdkbkgk - did not match any documents"
    )
    chrome_driver.implicitly_wait(5)


def step_5(chrome_driver):
    try:
        elem = chrome_driver.find_element_by_id("idres")
        assert False, "Found element with id idres"
    except Exception:
        assert True
    chrome_driver.implicitly_wait(0)


def test_no_result_found(chrome_driver):
    chrome_driver.get(test_config["base_url"])
    try:
        global_step_wait = test_config["step_wait"]
        chrome_driver.implicitly_wait(global_step_wait)
        step_1(chrome_driver)
        step_2(chrome_driver)
        step_3(chrome_driver)
        step_4(chrome_driver)
        step_5(chrome_driver)
    except Exception as ex:
        print(ex)
        chrome_driver.quit()
