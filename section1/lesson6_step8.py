import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/find_xpath_form'
browser = webdriver.Firefox()
try:
    browser.get(link)
    input1 = browser.find_element(by='tag name', value='input')
    input1.send_keys("Irina")
    input2 = browser.find_element(by='name', value="last_name")
    input2.send_keys("Lomskaya")
    input3 = browser.find_element(by='class name', value='form-control.city')
    input3.send_keys("SPB")
    input4 = browser.find_element(by='id', value='country')
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

