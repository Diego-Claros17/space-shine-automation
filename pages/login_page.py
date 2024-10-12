from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.header_page_locators import HeaderPageLocators
from config.config import Config


class LoginPage(BasePage):
    def login(self, email, password):
        self.navigate_to(Config.BASE_URL)
        self.click_element(HeaderPageLocators.ACCOUNT_LINK)
        self.fill_field(LoginPageLocators.EMAIL_FIELD, email)
        self.fill_field(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
