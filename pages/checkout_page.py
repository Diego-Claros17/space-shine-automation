from telnetlib import EC

from selenium.common import TimeoutException

from locators.cart_page_locators import CartPageLocators
from locators.product_page_locators import ProductPageLocators
from pages.product_page import ProductPage
from locators.checkout_page_locators import CheckoutPageLocators
from config.checkout_test_data import CheckoutTestData
from locators.account_page_locators import AccountPageLocators

import time
class CheckoutPage(ProductPage):  # Hereda de BasePage

    """def fill_card_details(self, card_number, expiration_date, cvv):
        #iframes = self.driver.find_elements(CheckoutPageLocators.CARD_IFRAME)
        iframes = self.driver.find_elements(*CheckoutPageLocators.CARD_IFRAME)

        self.driver.switch_to.frame(iframes[0])
        self.fill_field(CheckoutPageLocators.CARD_NUMBER_FIELD, card_number)
        self.driver.switch_to.default_content()  # Volver al contexto principal
        self.driver.switch_to.frame(iframes[1])
        self.fill_field(CheckoutPageLocators.EXP_DATE_FIELD, expiration_date)
        self.driver.switch_to.default_content()  # Volver al contexto principal
        self.driver.switch_to.frame(iframes[2])
        self.fill_field(CheckoutPageLocators.SECURITY_CODE_FIELD, cvv)
        self.driver.switch_to.default_content()  # Volver al contexto principal al final"""

    def fill_card_details(self, card_number, expiration_date, cvv):
        # Encuentra todos los iframes en la página (ya especificados en CheckoutPageLocators)
        iframes = self.driver.find_elements(*CheckoutPageLocators.CARD_IFRAME)

        # Cambiar al primer iframe y pegar el número de tarjeta
        self.driver.switch_to.frame(iframes[0])
        card_number_field = self.driver.find_element(*CheckoutPageLocators.CARD_NUMBER_FIELD)
        card_number_field.clear()
        card_number_field.send_keys(card_number)  # Pegamos el número de tarjeta
        self.driver.switch_to.default_content()  # Volver al contexto principal

        # Cambiar al segundo iframe y pegar primero el mes y luego el año
        self.driver.switch_to.frame(iframes[1])
        expiration_date_field = self.driver.find_element(*CheckoutPageLocators.EXP_DATE_FIELD)
        expiration_date_field.clear()

        # Dividimos el valor de expiration_date en mes y año
        month = expiration_date[:2]  # Extrae los primeros dos dígitos para el mes
        year = expiration_date[2:]  # Extrae los últimos dos dígitos para el año

        # Enviar primero el mes y luego el año
        expiration_date_field.send_keys(month)  # Pegamos el mes
        expiration_date_field.send_keys(year)  # Pegamos el año
        self.driver.switch_to.default_content()  # Volver al contexto principal

        # Cambiar al tercer iframe y pegar el código de seguridad
        self.driver.switch_to.frame(iframes[2])
        security_code_field = self.driver.find_element(*CheckoutPageLocators.SECURITY_CODE_FIELD)
        security_code_field.clear()
        security_code_field.send_keys(cvv)  # Pegamos el código de seguridad
        self.driver.switch_to.default_content()  # Volver al contexto principal

    def buy_product(self,email, first_name, last_name, address, apartment, city, phone, card_number, exp_date, security_code):
        # Navegar a la página de checkout
        self.add_to_cart()  # Método para añadir el producto al carrito
        self.click_element(ProductPageLocators.CART_BTN_LINK)  # Hacer clic en el carrito
        self.click_element(CartPageLocators.CHECKOUT_BTN_LINK)  # Ir al checkout
        # Completar los campos de información personal
        self.fill_field(CheckoutPageLocators.EMAIL_FIELD, email)
        self.fill_field(CheckoutPageLocators.FIRST_NAME_FIELD, first_name)
        self.fill_field(CheckoutPageLocators.LAST_NAME_FIELD, last_name)
        self.fill_field(CheckoutPageLocators.ADDRESS_FIELD, address)
        self.fill_field(CheckoutPageLocators.APARTMENT_FIELD, apartment)
        self.fill_field(CheckoutPageLocators.CITY_FIELD, city)
        self.fill_field(CheckoutPageLocators.PHONE_FIELD, phone)
        self.fill_card_details(
            card_number,
            exp_date,
            security_code)
        self.click_element(CheckoutPageLocators.PAY_NOW_BTN)

def assert_text_paid(self, locator, expected_text):
    try:
        # Asegúrate de que el locator sea una tupla válida como (By.XPATH, "xpath_value")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        actual_text = element.text.strip()
        assert expected_text == actual_text, \
            f"Expected text '{expected_text}' but got '{actual_text}' at element located by {locator}."
    except TimeoutException:
        raise AssertionError(
            f"Element located by {locator} with expected text '{expected_text}' was not found.")



