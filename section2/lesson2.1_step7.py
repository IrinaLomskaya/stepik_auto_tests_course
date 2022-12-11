import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html" #
browser = webdriver.Firefox()

try:
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x_at_el = x_element.get_attribute("valuex")
    x = x_at_el
    y = calc(x)
    form = browser.find_element(By.CSS_SELECTOR, "#answer")
    form.send_keys(y)
    ch_box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    ch_box.click()
    radio_b = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio_b.click()
    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()

finally:
    time.sleep(5)
    browser.quit()
