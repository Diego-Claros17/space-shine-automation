class AccountPageSelectors:
    LATEST_ORDER_ROW = "//table[@class='order-history']//tbody/tr[1]"
    ORDER_NUMBER_ELEMENT = ".//a[@aria-label]"

    # Dentro de esa fila, localiza la celda del estado de pago
    PAYMENT_STATUS_ELEMENT = ".//td[@data-label='Payment status']"
    LOGOUT_BUTTON = "[data-test='logout-icon']"
