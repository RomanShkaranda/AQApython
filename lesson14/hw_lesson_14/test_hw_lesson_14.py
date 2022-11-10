from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
import time


def test_swag_labs_01():

    user_name = 'problem_user'
    password = 'secret_sauce'

    chrome_driver = Chrome('chromedriver.exe')
    chrome_driver.maximize_window()
    chrome_driver.get('https://www.saucedemo.com/')
    time.sleep(2)

    user_name_locator = '//input[@id="user-name"]'
    user_name_element = chrome_driver.find_element(By.XPATH, user_name_locator)
    user_name_element.clear()
    user_name_element.send_keys(user_name)
    time.sleep(2)

    password_locator = '//input[@id="password"]'
    password_element = chrome_driver.find_element(By.XPATH, password_locator)
    password_element.clear()
    password_element.send_keys(password)
    time.sleep(2)

    login_button_locator = '//input[@id="login-button"]'
    login_button_element = chrome_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    time.sleep(2)

    cart_button_locator = '//div[@id="shopping_cart_container"]'
    cart_button_element = chrome_driver.find_element(By.XPATH, cart_button_locator)
    is_logout_button = cart_button_element.is_displayed()

    assert is_logout_button is True, 'Invalid input data'

    chrome_driver.quit()


