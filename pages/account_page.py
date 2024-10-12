from selenium.webdriver.common.by import By

from locators.product_page_locators import ProductPageLocators
from pages.product_page import ProductPage
from locators.checkout_page_locators import CheckoutPageLocators
from locators.account_page_locators import AccountPageLocators
from pages.checkout_page import CheckoutPage


class AccountPage(CheckoutPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver  # Asegúrate de que el driver está disponible en la clase

    def get_latest_order_number(self):
        # Localiza el primer tr dentro del tbody usando find
        latest_order_row = self.find(AccountPageLocators.LATEST_ORDER_ROW)

        # Dentro de esa fila (latest_order_row), localiza el enlace del número de orden
        order_number_element = latest_order_row.find_element(*AccountPageLocators.ORDER_NUMBER_ELEMENT)

        # Extrae el número de orden, remueve el símbolo '#' y lo convierte a entero
        order_number = int(order_number_element.text.replace("#", ""))

        return order_number

    def get_latest_order_payment_status(driver):
        # Localiza el primer tr dentro del tbody
        latest_order_row = driver.find_element(AccountPageLocators.LATEST_ORDER_ROW)

        # Dentro de esa fila, localiza la celda del estado de pago
        payment_status_element = latest_order_row.find_element(AccountPageLocators.PAYMENT_STATUS_ELEMENT)

        # Extrae el texto del estado de pago (por ejemplo: 'Paid')
        payment_status = payment_status_element.text.strip()

        return payment_status
