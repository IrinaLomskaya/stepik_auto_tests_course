import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Firefox()

try:
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(1)
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    form = browser.find_element(By.CSS_SELECTOR, "#answer")
    form.send_keys(y)
    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()

finally:
    time.sleep(5)
    browser.quit()


