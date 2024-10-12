class CheckoutPageSelectors:
    CARD_IFRAME = "card-fields-iframe"
    EMAIL_FIELD = "email"
    COUNTRY_DROPDOWN = "Select0"
    FIRST_NAME_FIELD = "TextField0"
    LAST_NAME_FIELD = "TextField1"
    ADDRESS_FIELD = "TextField2"
    APARTMENT_FIELD = "TextField3"
    CITY_FIELD = "TextField4"
    PHONE_FIELD = "TextField5"
    CREDIT_CARD_RADIO_BTN = "basic-creditCards"

    # Selectores de los iframes usando data-card-fields
    CARD_NUMBER_IFRAME = "iframe[data-card-fields='number']"
    EXP_DATE_IFRAME = "iframe[data-card-fields='expiry']"
    SECURITY_CODE_IFRAME = "iframe[data-card-fields='verification_value']"

    # Selectores de los campos dentro de los iframes usando los IDs constantes
    CARD_NUMBER_FIELD = "input[id='number']"
    EXP_DATE_FIELD = "input[id='expiry']"
    SECURITY_CODE_FIELD = "input[id='verification_value']"
    PAY_NOW_BTN = "checkout-pay-button"
    PAYPAL_BTN = "basic-PAYPAL_EXPRESS"


    # Message errors
    EMAIL_ERROR_MSG = "error-for-email"
    LAST_NAME_ERROR_MSG = "error-for-TextField1"
    ADDRESS_ERROR_MSG = "error-for-TextField2"
    CITY_ERROR_MSG = "error-for-TextField4"
    PHONE_ERROR_MSG = "error-for-TextField5"
    CARD_NUMBER_ERROR_MSG = "error-for-number"
    EXPIRATION_DATE_ERROR_MSG = "error-for-expiry"
    SECURITY_CODE_ERROR_MSG = "error-for-verification_value"
    OPTIONAL_FIRST_NAME_MSG_ERROR = "error-for-first-name"
    OPTIONAL_ADDRESS_MSG_ERROR = "error-for-address"
    NAME_ON_CARD_ERROR_MSG = "error-for-name"
    DISCOUNT_FIELD = "ReductionsInput1"
    PAYMENT_ERROR_BANNER = "PaymentErrorBanner"


