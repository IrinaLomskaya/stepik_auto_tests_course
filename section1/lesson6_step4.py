import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/find_link_text'
browser = webdriver.Firefox()
try:
    browser.get(link)
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = browser.find_element(by='tag name', value='input')
    input1.send_keys("Irina")
    input2 = browser.find_element(by='name', value="last_name")
    input2.send_keys("Lomskaya")
    input3 = browser.find_element(by='class name', value='form-control.city')
    input3.send_keys("SPB")
    input4 = browser.find_element(by='id', value='country')
    input4.send_keys("Russia")
    button = browser.find_element(by='css selector', value='button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()

