from selenium.webdriver.common.by import By
from selectors_ui.login_page_selectors import LoginPageSelectors
from selectors_ui.cart_page_selectors import CartPageSelectors
from selectors_ui.product_page_selectors import ProductPageSelectors
from selectors_ui.checkout_page_selectors import CheckoutPageSelectors
from selectors_ui.checkout_page_selectors import CheckoutPageSelectors

class CheckoutPageLocators:
    CARD_IFRAME = (By.CLASS_NAME, CheckoutPageSelectors.CARD_IFRAME)

    EMAIL_FIELD = (By.ID, CheckoutPageSelectors.EMAIL_FIELD)
    COUNTRY_DROPDOWN = (By.ID, CheckoutPageSelectors.COUNTRY_DROPDOWN)
    FIRST_NAME_FIELD = (By.ID, CheckoutPageSelectors.FIRST_NAME_FIELD)
    LAST_NAME_FIELD = (By.ID, CheckoutPageSelectors.LAST_NAME_FIELD)
    ADDRESS_FIELD = (By.ID, CheckoutPageSelectors.ADDRESS_FIELD)
    APARTMENT_FIELD = (By.ID, CheckoutPageSelectors.APARTMENT_FIELD)
    CITY_FIELD = (By.ID, CheckoutPageSelectors.CITY_FIELD)
    PHONE_FIELD = (By.ID, CheckoutPageSelectors.PHONE_FIELD)
    CREDIT_CARD_RADIO_BTN = (By.ID, CheckoutPageSelectors.CREDIT_CARD_RADIO_BTN)

    CARD_NUMBER_IFRAME = (By.CSS_SELECTOR, "iframe[data-card-fields='number']")
    EXP_DATE_IFRAME = (By.CSS_SELECTOR, "iframe[data-card-fields='expiry']")
    SECURITY_CODE_IFRAME = (By.CSS_SELECTOR, "iframe[data-card-fields='verification_value']")

    # Definiciones para otros campos
    CARD_NUMBER_FIELD = (By.CSS_SELECTOR, "[data-current-field='number']")
    EXP_DATE_FIELD = (By.CSS_SELECTOR, "[data-current-field='expiry']")
    SECURITY_CODE_FIELD = (By.CSS_SELECTOR, "[data-current-field='verification_value']")


    PAY_NOW_BTN = (By.ID, CheckoutPageSelectors.PAY_NOW_BTN)
    PAYPAL_BTN = (By.ID, CheckoutPageSelectors.PAYPAL_BTN)
    #PAYPAL_BTN = (By.XPATH, CheckoutPageSelectors.PAYPAL_BTN)
    #Error messages
    EMAIL_ERROR_MSG = (By.ID, CheckoutPageSelectors.EMAIL_ERROR_MSG)
    LAST_NAME_ERROR_MSG = (By.ID, CheckoutPageSelectors.LAST_NAME_ERROR_MSG)
    ADDRESS_ERROR_MSG = (By.ID, CheckoutPageSelectors.ADDRESS_ERROR_MSG)
    CITY_ERROR_MSG = (By.ID, CheckoutPageSelectors.CITY_ERROR_MSG)
    PHONE_ERROR_MSG = (By.ID, CheckoutPageSelectors.PHONE_ERROR_MSG)
    CARD_NUMBER_ERROR_MSG = (By.ID, CheckoutPageSelectors.CARD_NUMBER_ERROR_MSG)
    EXPIRATION_DATE_ERROR_MSG = (By.ID, CheckoutPageSelectors.EXPIRATION_DATE_ERROR_MSG)
    SECURITY_CODE_ERROR_MSG = (By.ID, CheckoutPageSelectors.SECURITY_CODE_ERROR_MSG)
    NAME_ON_CARD_ERROR_MSG = (By.ID, CheckoutPageSelectors.NAME_ON_CARD_ERROR_MSG)
    OPTIONAL_FIRST_NAME_MSG_ERROR = (By.ID, CheckoutPageSelectors.OPTIONAL_FIRST_NAME_MSG_ERROR)
    OPTIONAL_ADDRESS_MSG_ERROR = (By.ID, CheckoutPageSelectors.OPTIONAL_ADDRESS_MSG_ERROR)
    DISCOUNT_FIELD = (By.ID, CheckoutPageSelectors.DISCOUNT_FIELD)
    PAYMENT_ERROR_BANNER = (By.ID, CheckoutPageSelectors.PAYMENT_ERROR_BANNER)
