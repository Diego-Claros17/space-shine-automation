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
        # Espera a que el botón esté visible y clicable
        button = self.wait.until(EC.element_to_be_clickable(locator))
        button.click()

    def get_text(self, locator):
        # Espera a que el campo esté visible y listo para interactuar
        field = self.wait.until(EC.visibility_of_element_located(locator))
        # Retorna el texto del campo
        return field.text

    def navigate_to(self, url):
        # Navega a una URL específica
        self.driver.get(url)
