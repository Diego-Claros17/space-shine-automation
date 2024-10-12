from config.checkout_test_data import CheckoutTestData
from config.login_test_data import LoginTestData
import time
from locators.checkout_page_locators import CheckoutPageLocators
from locators.product_page_locators import ProductPageLocators
from locators.account_page_locators import AccountPageLocators
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from config.test_data import TestData
from pages.checkout_page import CheckoutPage


def test_verify_successful_purchase_completion(driver):
    login_page = LoginPage(driver)
    checkout_page = AccountPage(driver)
    login_page.login(LoginTestData.EMAIL, LoginTestData.PASSWORD)
    last_order_number = checkout_page.get_latest_order_number()
    checkout_page.click_element(AccountPageLocators.LOGOUT_BUTTON)
    checkout_page.buy_product(
        email=TestData.EMAIL,
        first_name=TestData.FIRST_NAME,
        last_name=TestData.LAST_NAME,
        address=TestData.ADDRESS,
        apartment=TestData.APARTMENT,
        city=TestData.CITY,
        phone=TestData.PHONE,
        card_number=CheckoutTestData.CARD_NUMBER_VALID,
        exp_date=CheckoutTestData.EXPIRATION_DATE,
        security_code=CheckoutTestData.SECURITY_CODE
    )
    checkout_page.wait.until(lambda driver: "/thank-you" in checkout_page.driver.current_url)
    checkout_page.assert_url_contains("/thank-you")
    login_page.login(LoginTestData.EMAIL, LoginTestData.PASSWORD)
    new_last_order_number = checkout_page.get_latest_order_number()
    checkout_page.assert_text(AccountPageLocators.PAYMENT_STATUS_ELEMENT, "Paid")
    assert new_last_order_number == last_order_number + 1, f"Expected {last_order_number - 1}, but got {new_last_order_number}"



def test_verify_access_to_checkout_from_cart(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.add_to_cart()
    checkout_page.click_element(ProductPageLocators.CHECKOUT_BTN_LINK)
    assert '/checkouts/' in driver.current_url, f"Expected '/checkouts/' to be in the URL but got {driver.current_url}"


def test_verify_payment_form_accepts_valid_shipping_and_payment_info(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.buy_product(
        email=TestData.EMAIL,
        first_name=TestData.FIRST_NAME,
        last_name=TestData.LAST_NAME,
        address=TestData.ADDRESS,
        apartment=TestData.APARTMENT,
        city=TestData.CITY,
        phone=TestData.PHONE,
        card_number=CheckoutTestData.CARD_NUMBER_VALID,
        exp_date=CheckoutTestData.EXPIRATION_DATE,
        security_code=CheckoutTestData.SECURITY_CODE
    )


def test_verify_warning_on_payment_form_errors(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.buy_product(
        email=TestData.EMAIL,
        first_name=TestData.FIRST_NAME,
        last_name=TestData.LAST_NAME,
        address=TestData.ADDRESS,
        apartment=TestData.APARTMENT,
        city=TestData.CITY,
        phone=TestData.PHONE,
        card_number=TestData.EMPTY_TEXT,
        exp_date=TestData.EMPTY_TEXT,
        security_code=TestData.EMPTY_TEXT
    )
    checkout_page.click_element(CheckoutPageLocators.PAY_NOW_BTN)
def test_verify_confirmation_after_successful_purchase(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.buy_product(
        email=TestData.EMAIL,
        first_name=TestData.FIRST_NAME,
        last_name=TestData.LAST_NAME,
        address=TestData.ADDRESS,
        apartment=TestData.APARTMENT,
        city=TestData.CITY,
        phone=TestData.PHONE,
        card_number=CheckoutTestData.CARD_NUMBER_VALID,
        exp_date=CheckoutTestData.EXPIRATION_DATE,
        security_code=CheckoutTestData.SECURITY_CODE
    )
    checkout_page.wait.until(lambda driver: "/thank-you" in checkout_page.driver.current_url)
    checkout_page.assert_url_contains("/thank-you")



# Verificar que el sistema no permite avanzar al siguiente paso si hay campos requeridos vacíos en el formulario de pago.
def test_verify_cannot_proceed_with_empty_required_fields(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.add_to_cart()
    checkout_page.click_element(ProductPageLocators.CHECKOUT_BTN_LINK)
    checkout_page.click_element(CheckoutPageLocators.PAY_NOW_BTN)
    time.sleep(2)
    checkout_page.assert_error_message(
        CheckoutPageLocators.EMAIL_ERROR_MSG,
        CheckoutTestData.EMAIL_ERROR_MSG,
        "Email error message is incorrect"
    )

    checkout_page.assert_error_message(
        CheckoutPageLocators.LAST_NAME_ERROR_MSG,
        CheckoutTestData.LAST_NAME_ERROR_MSG,
        "Last name error message is incorrect"
    )

    checkout_page.assert_error_message(
        CheckoutPageLocators.ADDRESS_ERROR_MSG,
        CheckoutTestData.ADDRESS_ERROR_MSG,
        "Address error message is incorrect"
    )

    checkout_page.assert_error_message(
        CheckoutPageLocators.CITY_ERROR_MSG,
        CheckoutTestData.CITY_ERROR_MSG,
        "City error message is incorrect"
    )

    checkout_page.assert_error_message(
        CheckoutPageLocators.PHONE_ERROR_MSG,
        CheckoutTestData.PHONE_ERROR_MSG,
        "Phone error message is incorrect"
    )

    checkout_page.assert_error_message(
        CheckoutPageLocators.CARD_NUMBER_ERROR_MSG,
        CheckoutTestData.CARD_NUMBER_ERROR_MSG,
        "Card number error message is incorrect"
    )

    checkout_page.assert_error_message(
        CheckoutPageLocators.EXPIRATION_DATE_ERROR_MSG,
        CheckoutTestData.EXPIRATION_DATE_ERROR_MSG,
        "Expiration date error message is incorrect"
    )

    checkout_page.assert_error_message(
        CheckoutPageLocators.SECURITY_CODE_ERROR_MSG,
        CheckoutTestData.SECURITY_CODE_ERROR_MSG,
        "Security code error message is incorrect"
    )

    checkout_page.assert_error_message(
        CheckoutPageLocators.NAME_ON_CARD_ERROR_MSG,
        CheckoutTestData.NAME_ON_CARD_ERROR_MSG,
        "Name on card error message is incorrect"
    )


# Verificar que el sistema muestra un error si se ingresa una tarjeta de crédito con fecha de expiración pasada.
def test_verify_error_message_for_expired_credit_card(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.add_to_cart()
    checkout_page.click_element(ProductPageLocators.CHECKOUT_BTN_LINK)
    checkout_page.fill_card_details(
        card_number=CheckoutTestData.CARD_NUMBER_VALID,
        expiration_date=CheckoutTestData.EXPIRED_EXPIRATION_DATE,
        cvv=CheckoutTestData.SECURITY_CODE)
    checkout_page.click_element(CheckoutPageLocators.PAY_NOW_BTN)
    checkout_page.assert_error_message(
        CheckoutPageLocators.EXPIRATION_DATE_ERROR_MSG,
        CheckoutTestData.EXPIRATION_DATE_ERROR_MSG,
     "Expiration date error message is incorrect"
    )



# Verify that the payment form accepts valid shipping and payment info


def test_verify_warning_message_for_empty_shipping_address(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.buy_product(
        email=TestData.EMAIL,
        first_name=TestData.FIRST_NAME,
        last_name=TestData.LAST_NAME,
        address=TestData.EMPTY_TEXT,
        apartment=TestData.APARTMENT,
        city=TestData.CITY,
        phone=TestData.PHONE,
        card_number=CheckoutTestData.CARD_NUMBER_VALID,
        exp_date=CheckoutTestData.EXPIRATION_DATE,
        security_code=CheckoutTestData.SECURITY_CODE
    )
    checkout_page.assert_text(CheckoutPageLocators.ADDRESS_ERROR_MSG, CheckoutTestData.ADDRESS_ERROR_MSG)


def test_verify_error_message_for_invalid_phone_number(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.add_to_cart()
    checkout_page.click_element(ProductPageLocators.CHECKOUT_BTN_LINK)
    checkout_page.fill_field(CheckoutPageLocators.PHONE_FIELD, CheckoutTestData.INVALID_PHONE_NUMBER)
    checkout_page.click_element(CheckoutPageLocators.PAY_NOW_BTN)
    checkout_page.assert_error_text(CheckoutPageLocators.PHONE_ERROR_MSG, CheckoutTestData.INVALID_PHONE_ERROR_MSG)
def test_verify_error_message_for_incorrect_card_number(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.add_to_cart()
    checkout_page.click_element(ProductPageLocators.CHECKOUT_BTN_LINK)
    checkout_page.fill_card_details(
        card_number=CheckoutTestData.CARD_NUMBER_INCORRECT_NUMBER,
        expiration_date=CheckoutTestData.EXPIRATION_DATE,
        cvv=CheckoutTestData.SECURITY_CODE)
    checkout_page.click_element(CheckoutPageLocators.PAY_NOW_BTN)
    checkout_page.assert_error_text(CheckoutPageLocators.CARD_NUMBER_ERROR_MSG,
                                    CheckoutTestData.INVALID_CARD_NUMBER_ERROR_MSG)

def test_verify_error_message_for_declined_card(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.buy_product(
        email=TestData.EMAIL,
        first_name=TestData.FIRST_NAME,
        last_name=TestData.LAST_NAME,
        address=TestData.ADDRESS,
        apartment=TestData.APARTMENT,
        city=TestData.CITY,
        phone=TestData.PHONE,
        card_number=CheckoutTestData.CARD_NUMBER_DECLINED,
        exp_date=CheckoutTestData.EXPIRATION_DATE,
        security_code=CheckoutTestData.SECURITY_CODE
    )
    checkout_page.assert_text(CheckoutPageLocators.PAYMENT_ERROR_BANNER, CheckoutTestData.DECLINED_CARD_MSG)


def test_verify_error_message_for_invalid_expiration_month(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.add_to_cart()
    checkout_page.click_element(ProductPageLocators.CHECKOUT_BTN_LINK)
    checkout_page.fill_card_details(
        card_number=CheckoutTestData.CARD_NUMBER_VALID,
        expiration_date=CheckoutTestData.INVALID_EXPIRY_MONTH,
        cvv=CheckoutTestData.SECURITY_CODE)
    checkout_page.click_element(CheckoutPageLocators.PAY_NOW_BTN)
    checkout_page.assert_error_text(CheckoutPageLocators.EXPIRATION_DATE_ERROR_MSG,
                                    CheckoutTestData.EXPIRATION_DATE_ERROR_MSG)

def test_verify_error_message_for_invalid_expiration_year(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.add_to_cart()
    checkout_page.click_element(ProductPageLocators.CHECKOUT_BTN_LINK)
    checkout_page.fill_card_details(
        card_number=CheckoutTestData.CARD_NUMBER_VALID,
        expiration_date=CheckoutTestData.INVALID_EXPIRY_YEAR,
        cvv=CheckoutTestData.SECURITY_CODE)
    time.sleep(5)
    checkout_page.click_element(CheckoutPageLocators.PAY_NOW_BTN)
    checkout_page.assert_error_text(CheckoutPageLocators.EXPIRATION_DATE_ERROR_MSG,
                                    CheckoutTestData.EXPIRATION_DATE_ERROR_MSG)


def test_verify_no_error_message_for_optional_fields_empty(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.buy_product(
        email=TestData.EMAIL,
        first_name=TestData.FIRST_NAME,
        last_name=TestData.LAST_NAME,
        address=TestData.ADDRESS,
        apartment=TestData.EMPTY_TEXT,
        city=TestData.CITY,
        phone=TestData.PHONE,
        card_number=CheckoutTestData.CARD_NUMBER_DECLINED,
        exp_date=CheckoutTestData.EXPIRATION_DATE,
        security_code=CheckoutTestData.SECURITY_CODE
    )

def test_verify_paypal_payment_method_selection(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.add_to_cart()
    checkout_page.click_element(ProductPageLocators.CHECKOUT_BTN_LINK)
    checkout_page.click_element(CheckoutPageLocators.PAYPAL_BTN)

