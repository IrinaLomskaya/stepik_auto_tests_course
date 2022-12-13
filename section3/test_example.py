import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


@pytest.mark.parametrize('namber', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_guest_should_see_login_link(browser, namber):
    link = f"https://stepik.org/lesson/236{namber}/step/1"
    browser.get(link)
    answer = str(math.log(int(time.time())))
    #time.sleep(10)
    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,".ember-text-area"))
    )
    field = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")
    field.send_keys(answer)
    #говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    button.click()
    expected_result = "Correct!"
    actual_result = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    assert expected_result == actual_result.text, f"expected {expected_result}, got {actual_result.text}"