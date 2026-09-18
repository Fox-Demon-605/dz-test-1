# test_purchase.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_purchase(browser, url):
    wait = WebDriverWait(browser, 10)

    browser.get(url)


    username_field = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    username_field.send_keys("standard_user")

    password_field = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_field.send_keys("secret_sauce")

    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()


    add_to_cart_button = wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    add_to_cart_button.click()

    cart_icon = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart_icon.click()


    checkout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

    first_name_field = wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )
    first_name_field.send_keys("Ivan")

    last_name_field = wait.until(
        EC.visibility_of_element_located((By.ID, "last-name"))
    )
    last_name_field.send_keys("Ivanov")

    postal_code_field = wait.until(
        EC.visibility_of_element_located((By.ID, "postal-code"))
    )
    postal_code_field.send_keys("123456")

    continue_button = wait.until(
        EC.element_to_be_clickable((By.ID, "continue"))
    )
    continue_button.click()


    finish_button = wait.until(
        EC.element_to_be_clickable((By.ID, "finish"))
    )
    finish_button.click()


    success_message = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text

    assert success_message == "Thank you for your order!"