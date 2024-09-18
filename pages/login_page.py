from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.header_page_locators import HeaderPageLocators
from config.config import Config

class LoginPage(BasePage):  # Hereda de BasePage
    def login(self, email, password):
        # Navega a la página de login
        self.navigate_to(Config.LOGIN_URL)
        # Llena los campos de email y contraseña
        self.click_element(HeaderPageLocators.ACCOUNT_LINK)
        self.fill_field(LoginPageLocators.EMAIL_FIELD, email)
        self.fill_field(LoginPageLocators.PASSWORD_FIELD, password)
        # Clic en el botón de login
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
