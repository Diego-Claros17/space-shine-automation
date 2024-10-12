from locators.header_page_locators import HeaderPageLocators
from config.config import Config
from pages.base_page import BasePage
from locators.product_page_locators import ProductPageLocators
from config.test_data import TestData


class ProductPage(BasePage):
    def add_to_cart(self):
        self.navigate_to(TestData.ASTRONAUT_PROJECTOR_URL)
        self.click_element(ProductPageLocators.ADD_TO_CART_BUTTON)

