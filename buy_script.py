from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://www.saucedemo.com/"

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 1000)

try:
    driver.get(URL)

    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.presence_of_element_located((By.ID, "checkout"))).click()

    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Ivan")
    driver.find_element(By.ID, "last-name").send_keys("Ivanov")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    wait.until(EC.presence_of_element_located((By.ID, "finish"))).click()

    success_message = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text
    print("Результат:", success_message)
    assert success_message == "Thank you for your order!"

finally:
    time.sleep(2)
    driver.quit()