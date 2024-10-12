import time

import allure
import pytest

from pages.login_page import LoginPage
from config.test_data import TestData
from config.login_test_data import LoginTestData
from locators.login_page_locators import LoginPageLocators


#Verify successful login with valid credentials
def test_verify_successful_login_with_valid_credentials(driver):
    # Create instance of LoginPage
    login_page = LoginPage(driver)
    login_page.login(TestData.EMAIL, TestData.PASSWORD)
    #assert login_page.assert_url_contains("/account")
    assert login_page.assert_url_contains("/account")

#Verify error message when login attempt with empty credentials
@allure.tag('defect', 'expected_failure')
#@pytest.mark.xfail(reason="This test is destined to fail due to a known defect")
def test_verify_error_message_with_empty_credentials(driver):
    login_page = LoginPage(driver)
    login_page.login(TestData.EMPTY_EMAIL, TestData.EMPTY_PASSWORD)
    assert login_page.get_text(LoginPageLocators.LOGIN_ERROR_MSG) == "Empty credentials.", "The error message for empty credentials is incorrect."

#Verify error message when login attempt with invalid credentials
def test_verify_error_message_with_invalid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.login(TestData.WRONG_EMAIL, TestData.WRONG_PASSWORD)
    login_page.assert_error_text(LoginPageLocators.LOGIN_ERROR_MSG, "Incorrect email or password.")


# Verificar que el campo de correo electrónico acepta direcciones válidas.

def test_verify_email_field_accepts_valid_emails(driver):
    login_page = LoginPage(driver)  # Instancia de la página correspondiente
    login_page.login(LoginTestData.EMAIL, TestData.EMPTY_TEXT)
    error_message = login_page.get_text(LoginPageLocators.LOGIN_ERROR_MSG)
    assert error_message != "Incorrect Email Format", \
    f"Test failed because the error message was '{error_message}', indicating an invalid email format."

# Verificar el botón "Recordar mi contraseña" funcional.
def test_verify_remember_password_button_functionality(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to(LoginTestData.LOGIN_URL)
    login_page.click_element(LoginPageLocators.FORGOT_PASSWORD_BTN)
    login_page.assert_url("https://spaceshine.shop/account/login#recover")

# Verificar que el campo de correo electrónico no acepta caracteres especiales inválidos.
@allure.tag('defect', 'expected_failure')
#@pytest.mark.xfail(reason="This test is destined to fail due to a known defect")
def test_verify_email_field_rejects_invalid_characters(driver):
    login_page = LoginPage(driver)
    login_page.login(TestData.INVALID_CHARACTERS_EMAIL, TestData.PASSWORD)
    assert login_page.get_text(
        LoginPageLocators.LOGIN_ERROR_MSG) == "Invalid characters in email field", "The error message for invalid credentials is incorrect."

@allure.tag('defect', 'expected_failure')
#@pytest.mark.xfail(reason="This test is destined to fail due to a known defect")
def test_verify_error_message_with_invalid_email_format(driver):
    login_page = LoginPage(driver)
    login_page.login(TestData.INVALID_EMAIL, TestData.PASSWORD)
    assert login_page.get_text(
        LoginPageLocators.LOGIN_ERROR_MSG) == "Invalid email", "The error message for invalid credentials is incorrect."

# Verificar que el sistema muestra un mensaje de error al ingresar una contraseña muy corta.
@allure.tag('defect', 'expected_failure')
#@pytest.mark.xfail(reason="This test is destined to fail due to a known defect")
def test_verify_error_message_with_short_password(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginTestData.EMAIL, LoginTestData.SHORT_PASSWORD)
    login_page.assert_error_text(LoginPageLocators.LOGIN_ERROR_MSG,
                                 "Your password is too short. It must be at least 8 characters long")

@allure.tag('defect', 'expected_failure')
#@pytest.mark.xfail(reason="This test is destined to fail due to a known defect")
def test_verify_error_message_with_long_password(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginTestData.EMAIL, LoginTestData.LONG_PASSWORD)
    login_page.assert_error_text(LoginPageLocators.LOGIN_ERROR_MSG,
                                     "Your password is too long. It must not exceed 20 characters.")
