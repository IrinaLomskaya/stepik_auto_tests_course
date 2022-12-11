import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Firefox()

try:
    browser.get(link)
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()
    form = browser.find_element(By.CSS_SELECTOR, "#answer")
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    form.send_keys(y)
    btn = browser.find_element(By.CSS_SELECTOR, "#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()

finally:
    time.sleep(5)
    browser.quit()