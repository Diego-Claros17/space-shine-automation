from pages.base_page import BasePage
from locators.product_page_locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        self.click_element(ProductPageLocators.ADD_TO_CART_BUTTON)

    def verify_product_name(self):
        return self.get_text(ProductPageLocators.PRODUCT_NAME)
