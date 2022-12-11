import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x, y):
  return str(int(x) + int(y))

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Firefox()

try:
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    x = x_element.text
    y = y_element.text
    sum = calc(x, y)
    form = Select(browser.find_element(By.TAG_NAME, "select"))
    form.select_by_value(sum)
    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()

finally:
    time.sleep(5)
    browser.quit()
