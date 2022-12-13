from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login_email")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#id_login_password")