from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import unittest
import time

class TestLesson3(unittest.TestCase):
    def test_01(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Firefox()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        f_name = browser.find_element(By.CSS_SELECTOR, ".first_block > div:nth-child(1) > input:nth-child(2)")
        f_name.send_keys("Irina")
        l_name = browser.find_element(By.CSS_SELECTOR, ".first_block > div:nth-child(2) > input:nth-child(2)")
        l_name.send_keys("Lomskaya")
        email = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        email.send_keys("someone@bla.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_02(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Firefox()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        f_name = browser.find_element(By.CSS_SELECTOR, ".first_block > div:nth-child(1) > input:nth-child(2)")
        f_name.send_keys("Irina")
        l_name = browser.find_element(By.CSS_SELECTOR, ".first_block > div:nth-child(2) > input:nth-child(2)")
        l_name.send_keys("Lomskaya")
        email = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        email.send_keys("someone@bla.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == '__main__':
    unittest.main()
