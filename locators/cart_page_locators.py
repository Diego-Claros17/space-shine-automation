from selenium.webdriver.common.by import By
from selectors_ui.login_page_selectors import LoginPageSelectors
from selectors_ui.cart_page_selectors import CartPageSelectors
from selectors_ui.product_page_selectors import ProductPageSelectors


class CartPageLocators:
    REMOVE_PRODUCT_BTN = (By.ID, CartPageSelectors.REMOVE_PRODUCT_BTN)
    CART_EMPTY_TEXT = (By.CLASS_NAME, CartPageSelectors.CART_EMPTY_TEXT)
    TOTAL_PRICE = (By.CSS_SELECTOR, CartPageSelectors.TOTAL_PRICE)
    CHECKOUT_BTN_LINK = (By.ID, CartPageSelectors.CHECKOUT_BTN_LINK)
