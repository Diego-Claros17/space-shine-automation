from selenium.webdriver.common.by import By
from selectors_ui.login_page_selectors import LoginPageSelectors
from selectors_ui.cart_page_selectors import CartPageSelectors
from selectors_ui.account_page_selectors import AccountPageSelectors
from selectors_ui.product_page_selectors import ProductPageSelectors


class AccountPageLocators:
    REMOVE_PRODUCT_BTN = (By.ID, CartPageSelectors.REMOVE_PRODUCT_BTN)
    LATEST_ORDER_ROW = (By.XPATH, AccountPageSelectors.LATEST_ORDER_ROW)
    ORDER_NUMBER_ELEMENT = (By.XPATH, AccountPageSelectors.ORDER_NUMBER_ELEMENT)
    PAYMENT_STATUS_ELEMENT = (By.XPATH, AccountPageSelectors.PAYMENT_STATUS_ELEMENT)
    LOGOUT_BUTTON = (By.CSS_SELECTOR, AccountPageSelectors.LOGOUT_BUTTON)