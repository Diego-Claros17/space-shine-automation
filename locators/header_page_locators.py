from selenium.webdriver.common.by import By
from selectors_ui.login_page_selectors import LoginPageSelectors
from selectors_ui.header_page_selectors import HeaderPageSelectors


class HeaderPageLocators:
    ACCOUNT_LINK = (By.CSS_SELECTOR, HeaderPageSelectors.ACCOUNT_LINK)
    HOME_LINK = (By.CSS_SELECTOR, HeaderPageSelectors.HOME_LINK)
    CATALOG_LINK = (By.CSS_SELECTOR, HeaderPageSelectors.CATALOG_LINK)
    CONTACT_LINK = (By.CSS_SELECTOR, HeaderPageSelectors.CONTACT_LINK)
    MIDDLE_LOGO_LINK = (By.CSS_SELECTOR, HeaderPageSelectors.MIDDLE_LOGO_LINK)
    SIDE_LOGO_LINK = (By.CSS_SELECTOR, HeaderPageSelectors.SIDE_LOGO_LINK)
    CART_LOGO_LINK = (By.ID, HeaderPageSelectors.CART_LOGO_LINK)
    # CART_LOGO_LINK = (By.ID, "cart-icon-bubble")
