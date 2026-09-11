# test_purchase.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_purchase(browser, url):
    wait = WebDriverWait(browser, 10)

    browser.get(url)

    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    wait.until(
        EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()

    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.presence_of_element_located((By.ID, "checkout"))).click()

    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Ivan")
    browser.find_element(By.ID, "last-name").send_keys("Ivanov")
    browser.find_element(By.ID, "postal-code").send_keys("123456")
    browser.find_element(By.ID, "continue").click()

    wait.until(EC.presence_of_element_located((By.ID, "finish"))).click()

    success_message = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text

    assert success_message == "Thank you for your order!"