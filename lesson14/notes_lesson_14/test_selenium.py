import time

from selenium.webdriver import Chrome


def test_01():
    driver_chrome = Chrome('chromedriver.exe')
    driver_chrome.maximize_window()
    driver_chrome.get('https://admin-demo.nopcommerce.com/')
    time.sleep(3)
    actual_title = driver_chrome.title
    expected_title = 'Your store. Login'
    assert actual_title == expected_title

    driver_chrome.quit()

def test_login():
    driver_chrome = Chrome('chromedriver.exe')
    driver_chrome.maximize_window()
    driver_chrome.get('https://admin-demo.nopcommerce.com')
    time.sleep(100)

    login = 'admin@yourstore.com'
    password = 'admin'

    email_input_locator = '//input[@id="Email"]'
    email_input_element = driver_chrome.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    time.sleep(2)
    email_input_element.send_keys()

