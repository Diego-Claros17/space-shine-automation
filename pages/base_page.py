import re

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Config.DEFAULT_WAIT_TIME)

    def fill_field(self, locator, text):
        # Espera a que el campo esté visible y listo para interactuar
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(text)

    def click_element(self, locator):
        button = self.wait.until(EC.element_to_be_clickable(locator))
        button.click()

    def get_text(self, locator):
        # Espera a que el campo esté visible y listo para interactuar
        field = self.wait.until(EC.visibility_of_element_located(locator))
        # Retorna el texto del campo
        return field.text

    def navigate_to(self, url):
        self.driver.get(url)

    def get_value(self, locator):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        return field.get_attribute("value")


    def wait_for_element_to_be_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element with locator {locator} not visible after the default wait time")

    def assert_error_message(self, locator, expected_message, error_description):
        error_element = self.wait.until(EC.visibility_of_element_located(locator))
        actual_message = error_element.text
        assert actual_message == expected_message, error_description

    def assert_error_text(self, locator, expected_message):
        try:
            error_element = self.wait.until(EC.visibility_of_element_located(locator))
            actual_message = error_element.text.strip()
            assert expected_message in actual_message, \
                f"Expected '{expected_message}' but got '{actual_message}' at element located by {locator}."
        except TimeoutException:
            raise AssertionError(
                f"Element located by {locator} with expected message '{expected_message}' was not found.")

    def assert_text(self, locator, expected_text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            actual_text = element.text.strip()
            assert expected_text == actual_text, \
                f"Expected text '{expected_text}' but got '{actual_text}' at element located by {locator}."

        except TimeoutException:
            raise AssertionError(
                f"Element located by {locator} with expected text '{expected_text}' was not found.")

    def assert_url_contains(self, expected_url_fragment):
        try:
            self.wait.until(EC.url_contains(expected_url_fragment))
            return True
        except TimeoutException:
            current_url = self.driver.current_url
            error_message = f"Expected fragment '{expected_url_fragment}' not found in the current URL: {current_url}"
            print(error_message)
            return False

    def assert_url(self, expected_url):
        try:
            # Asegúrate de tener un tiempo de espera adecuado
            self.wait.until(lambda driver: expected_url == driver.current_url,
                            f"Timed out waiting for URL to be '{expected_url}'")
            return True
        except TimeoutException:
            current_url = self.driver.current_url
            error_message = f"Expected URL '{expected_url}' but got '{current_url}'"
            print(error_message)  # Imprime el mensaje de error para depuración
            raise AssertionError(error_message)  # Levanta una excepción de assertion

    def extract_integer_from_element(self, locator):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        element_text = field.text
        match = re.search(r'\d+(\.\d+)?', element_text)
        if match:
            return float(match.group())
        return 0
        # Método reutilizable para cambiar a un iframe y llenar un campo

    def switch_to_iframe_and_fill(self, iframe_locator, field_locator, value):
        # Encuentra todos los iframes en la página
        iframes = self.driver.find_elements(By.TAG_NAME, 'iframe')

        for index, iframe in enumerate(iframes):
            self.driver.switch_to.frame(iframe)
            try:
                # Esperar a que el campo esté clickeable dentro del iframe
                field = self.wait.until(EC.element_to_be_clickable(field_locator))
                if field:
                    # Si encontramos el campo, llenamos el valor
                    field.clear()
                    field.send_keys(value)
                    print(f"Field found in iframe {index}, filling value.")
                    break
            except TimeoutException:
                # Si no se encuentra el campo, regresar al contexto principal y continuar
                print(f"Field not found in iframe {index}, switching back.")
                self.driver.switch_to.default_content()

        # Volver al contexto principal después de interactuar con el campo
        self.driver.switch_to.default_content()

    """def switch_to_iframe_and_fill(self, iframe_locator, field_locator, value):
        # Esperar a que el iframe esté disponible y cambiar al contexto del iframe
        iframe = self.wait.until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))
        self.fill_field(field_locator, value)
        # No cambiamos de contexto aquí; se hace una vez en el método principal"""
    """    def find_element(self, by, value):
        return self.driver.find_element(by, value)"""

    def find(self, locator):
        return self.driver.find_element(*locator)  # Usa el locator como tupla (By, value)
