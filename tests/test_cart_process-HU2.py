import allure

from locators.product_page_locators import ProductPageLocators
from locators.header_page_locators import HeaderPageLocators
from locators.cart_page_locators import CartPageLocators
from config.test_data import TestData
from config.cart_test_data import CartTestData
from config.product_test_data import ProductTestData
from pages.product_page import ProductPage

def test_verify_user_can_access_cart_page(driver):
    product_page = ProductPage(driver)
    product_page.navigate_to(TestData.ASTRONAUT_PROJECTOR_URL)
    product_page.click_element(HeaderPageLocators.CART_LOGO_LINK)
    product_page.assert_url(CartTestData.CART_URL)

def test_verify_product_added_to_cart_successfully(driver):
    product_page = ProductPage(driver)
    product_page.add_to_cart()
    assert product_page.get_text(
        ProductPageLocators.ADD_TO_CART_CONFIRMATION) == "Item added to your cart", "The error message for empty credentials is incorrect."

def test_verify_product_removed_from_cart_successfully(driver):
    product_page = ProductPage(driver)
    product_page.add_to_cart()
    product_page.click_element(ProductPageLocators.CART_BTN_LINK)
    product_page.click_element(CartPageLocators.REMOVE_PRODUCT_BTN)
    cart_empty_text = product_page.get_text(CartPageLocators.CART_EMPTY_TEXT)
    assert cart_empty_text == "Your cart is empty", "Cart empty text is incorrect"

# review
def test_verify_product_count_reduces_after_removal(driver):
    product_page = ProductPage(driver)
    product_page.navigate_to(TestData.ASTRONAUT_PROJECTOR_URL)
    product_page.click_element(ProductPageLocators.QUANTITY_INCREASE_BTN)
    initial_value = int(product_page.get_value(ProductPageLocators.QUANTITY_VALUE))
    product_page.click_element(ProductPageLocators.QUANTITY_DECREASE_BTN)
    new_value = int(product_page.get_value(ProductPageLocators.QUANTITY_VALUE))
    assert new_value == initial_value - 1, f"Expected {initial_value - 1}, but got {new_value}"


# Verificar que el subtotal del carrito se actualiza correctamente después de agregar múltiples productos.
def test_verify_cart_subtotal_after_adding_multiple_products(driver):
    product_page = ProductPage(driver)
    product_page.navigate_to(TestData.ASTRONAUT_PROJECTOR_URL)
    astronaut_price = product_page.extract_integer_from_element(ProductPageLocators.PRODUCT_PRICE)
    product_page.click_element(ProductPageLocators.ADD_TO_CART_BUTTON)
    product_page.wait_for_element_to_be_visible(ProductPageLocators.ADD_TO_CART_CONFIRMATION)
    product_page.navigate_to(ProductTestData.KID_ASTRONAUT_PROJECTOR_URL)
    kid_astronaut_price = product_page.extract_integer_from_element(ProductPageLocators.PRODUCT_PRICE)
    product_page.click_element(ProductPageLocators.ADD_TO_CART_BUTTON)
    product_page.wait_for_element_to_be_visible(ProductPageLocators.ADD_TO_CART_CONFIRMATION)
    product_page.navigate_to(ProductTestData.DINOSAUR_PROJECTOR_URL)
    dinosaur_astronaut_price = product_page.extract_integer_from_element(ProductPageLocators.PRODUCT_PRICE)
    total_sum = astronaut_price + kid_astronaut_price + dinosaur_astronaut_price
    product_page.click_element(ProductPageLocators.ADD_TO_CART_BUTTON)
    product_page.click_element(ProductPageLocators.CART_BTN_LINK)
    total_price = product_page.extract_integer_from_element(CartPageLocators.TOTAL_PRICE)
    assert total_price == total_sum, f"Expected {total_price}, but got {total_sum}"


# Verificar que el sistema muestra un mensaje de error si se intenta agregar al carrito un producto fuera de stock.
def test_verify_error_message_for_out_of_stock_product(driver):
    product_page = ProductPage(driver)
    product_page.navigate_to(ProductTestData.TEST_PRODUCT_URL)
    product_page.assert_error_text(ProductPageLocators.SOLD_OUT_MSG, "Sold out")


# Verificar que el sistema muestra un mensaje de error si el usuario intenta agregar una cantidad negativa de un producto.
@allure.tag('defect', 'expected_failure')
#@pytest.mark.xfail(reason="This test is destined to fail due to a known defect")
def test_verify_error_message_for_negative_product_quantity(driver):
    product_page = ProductPage(driver)
    product_page.navigate_to(TestData.ASTRONAUT_PROJECTOR_URL)
    product_page.fill_field(ProductPageLocators.QUANTITY_VALUE, -100)
    product_page.click_element(ProductPageLocators.ADD_TO_CART_BUTTON)
    negative_quantity_text = product_page.get_text(ProductPageLocators.STOCK_ERROR_MSG)
    assert negative_quantity_text == "Please enter a valid quantity", "Message that you cannot add negative products to the cart is incorrect"


def test_verify_cart_rejects_quantity_above_stock(driver):
    product_page = ProductPage(driver)
    product_page.navigate_to(TestData.ASTRONAUT_PROJECTOR_URL)
    product_page.fill_field(ProductPageLocators.QUANTITY_VALUE, 489948)
    product_page.click_element(ProductPageLocators.ADD_TO_CART_BUTTON)
    out_of_stock_text = product_page.get_text(ProductPageLocators.STOCK_ERROR_MSG)
    assert out_of_stock_text == "You can't add more Astronaut Light Projector to the cart.", "Message that you cannot add more products to the cart is incorrect"


def test_verify_total_price_updates_on_quantity_change(driver):
    product_page = ProductPage(driver)
    product_page.navigate_to(TestData.ASTRONAUT_PROJECTOR_URL)
    initial_price = product_page.extract_integer_from_element(ProductPageLocators.PRODUCT_PRICE)
    product_page.click_element(ProductPageLocators.QUANTITY_INCREASE_BTN)
    product_page.click_element(ProductPageLocators.ADD_TO_CART_BUTTON)
    product_page.click_element(ProductPageLocators.CART_BTN_LINK)
    total_price = product_page.extract_integer_from_element(CartPageLocators.TOTAL_PRICE)
    assert total_price == initial_price * 2, f"Expected {initial_price * 2}, but got {total_price}"


def test_verify_addition_on_cart_quantity(driver):
    product_page = ProductPage(driver)
    product_page.navigate_to(TestData.ASTRONAUT_PROJECTOR_URL)
    initial_value = int(product_page.get_value(ProductPageLocators.QUANTITY_VALUE))
    product_page.click_element(ProductPageLocators.QUANTITY_INCREASE_BTN)
    actual_value = int(product_page.get_value(ProductPageLocators.QUANTITY_VALUE))
    assert actual_value == 2, f"Expected {initial_value + 1}, but got {actual_value}"


def test_verify_empty_cart_message(driver):
    product_page = ProductPage(driver)
    product_page.navigate_to(CartTestData.CART_URL)
    product_page.assert_error_text(CartPageLocators.CART_EMPTY_TEXT, "Your cart is empty")


def test_verify_discounts_and_coupons_applied_to_cart(driver):
    product_page = ProductPage(driver)
    product_page.navigate_to(ProductTestData.DISCOUNT_URL)
    initial_price = product_page.extract_integer_from_element(ProductPageLocators.PRODUCT_PRICE)
    product_page.click_element(ProductPageLocators.ADD_TO_CART_BUTTON)
    product_page.click_element(ProductPageLocators.CART_BTN_LINK)
    discount_price = product_page.extract_integer_from_element(CartPageLocators.TOTAL_PRICE)
    assert discount_price == initial_price / 2, f"Expected {initial_price * 2}, but got {discount_price}"


def test_verify_message_after_removing_all_products_from_cart(driver):
    product_page = ProductPage(driver)
    product_page.add_to_cart()
    product_page.click_element(ProductPageLocators.CART_BTN_LINK)
    product_page.click_element(CartPageLocators.REMOVE_PRODUCT_BTN)
    product_page.assert_error_text(CartPageLocators.CART_EMPTY_TEXT, "Your cart is empty")
