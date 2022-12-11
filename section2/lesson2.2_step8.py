from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    f_name = browser.find_element(By.CSS_SELECTOR, "input.form-control:nth-child(2)")
    f_name.send_keys("Irina")
    l_name = browser.find_element(By.CSS_SELECTOR, "input.form-control:nth-child(4)")
    l_name.send_keys("Lomskaya")
    email = browser.find_element(By.XPATH, "/html/body/div/form/div/input[3]")
    email.send_keys("someone@bla.com")
    button_ch = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "1.txt")
    button_ch.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
