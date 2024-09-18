import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    # Ruta local al chromedriver.exe
    driver_path = "C:/Users/lclar/Documents/space-shine-automation/chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # Devuelve el navegador para ser utilizado en las pruebas
    yield driver

    # Cierra el navegador después de la prueba
    driver.quit()
