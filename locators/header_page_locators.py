from selenium.webdriver.common.by import By
from selectors_ui.login_page_selectors import LoginPageSelectors
from selectors_ui.header_page_selectors import HeaderPageSelectors


class HeaderPageLocators:
    ACCOUNT_LINK = (By.CSS_SELECTOR, HeaderPageSelectors.ACCOUNT_LINK)