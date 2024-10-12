from selenium.webdriver.common.by import By
from selectors_ui.login_page_selectors import LoginPageSelectors
from selectors_ui.product_page_selectors import ProductPageSelectors

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ProductPageSelectors.ADD_TO_CART_BUTTON)
    ADD_TO_CART_CONFIRMATION = (By.CSS_SELECTOR, ProductPageSelectors.ADD_TO_CART_CONFIRMATION)
    SOLD_OUT_MSG = (By.CSS_SELECTOR, ProductPageSelectors.SOLD_OUT_MSG)
    QUANTITY_INCREASE_BTN = (By.CSS_SELECTOR, ProductPageSelectors.QUANTITY_INCREASE_BTN)
    QUANTITY_DECREASE_BTN = (By.CSS_SELECTOR, ProductPageSelectors.QUANTITY_DECREASE_BTN)
    QUANTITY_VALUE = (By.CLASS_NAME, ProductPageSelectors.QUANTITY_VALUE)
    CART_BTN_LINK = (By.ID, ProductPageSelectors.CART_BTN_LINK)
    STOCK_ERROR_MSG = (By.CSS_SELECTOR, ProductPageSelectors.STOCK_ERROR_MSG)
    PRODUCT_PRICE = (By.CSS_SELECTOR, ProductPageSelectors.PRODUCT_PRICE)
    CHECKOUT_BTN_LINK = (By.ID, ProductPageSelectors.CHECKOUT_BTN_LINK)