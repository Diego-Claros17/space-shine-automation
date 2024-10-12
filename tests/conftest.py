import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    # Configura las opciones para Chrome
    chrome_options = Options()

    chrome_options.add_argument("--headless=old")
    #chrome_options.add_argument("--headless")

    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    # Utiliza WebDriverManager para manejar el chromedriver automáticamente
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    #driver.maximize_window()
    # Devuelve el navegador para ser utilizado en las pruebas
    yield driver
    driver.quit()

