import time
from pages.login_page import LoginPage
from config.test_data import TestData
from locators.login_page_locators import LoginPageLocators


#Verify successful login with valid credentials
def test_verify_successful_login_with_valid_credentials(driver):
    # Create instance of LoginPage
    login_page = LoginPage(driver)
    #login
    login_page.login(TestData.EMAIL, TestData.PASSWORD)
    #time.sleep(20)
    assert driver.current_url == TestData.ACCOUNT_URL , "El login falló. No se redirigió exactamente a la página de cuenta."

#Verify error message when login attempt with empty credentials
def test_verify_error_message_with_empty_credentials(driver):
    # Verify error message when login attempt with empty credentials
    login_page = LoginPage(driver)
    # Attempt to login with empty email and password
    login_page.login(TestData.EMPTY_EMAIL, TestData.EMPTY_PASSWORD)
    # Assert the error message is displayed
    assert login_page.get_text(LoginPageLocators.LOGIN_ERROR_MSG) == "Empty credentials.", "The error message for empty credentials is incorrect."
    # Assert the user is not redirected

#Verify error message when login attempt with invalid credentials
def test_verify_error_message_with_invalid_credentials(driver):
    # Verify error message when login attempt with invalid credentials
    login_page = LoginPage(driver)
    # Attempt to login with invalid email and password
    login_page.login(TestData.WRONG_EMAIL, TestData.WRONG_PASSWORD)
    # Assert the error message is displayed
    assert login_page.get_text(LoginPageLocators.LOGIN_ERROR_MSG) == "Incorrect", "The error message for invalid credentials is incorrect."
