from selenium.webdriver.common.by import By
from selectors_ui.login_page_selectors import LoginPageSelectors


class ProductPageLocators:
    EMAIL_FIELD = (By.ID, LoginPageSelectors.EMAIL_FIELD)
    PASSWORD_FIELD = (By.ID, LoginPageSelectors.PASSWORD_FIELD)
    LOGIN_BUTTON = (By.CSS_SELECTOR, LoginPageSelectors.LOGIN_BUTTON)
    LOGIN_ERROR_MSG = (By.CSS_SELECTOR, LoginPageSelectors.LOGIN_ERROR_MSG)
