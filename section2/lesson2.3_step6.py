import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Firefox()

try:
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, ".trollface")
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(3)
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    form = browser.find_element(By.CSS_SELECTOR, "#answer")
    form.send_keys(y)
    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()

finally:
    time.sleep(5)
    browser.quit()