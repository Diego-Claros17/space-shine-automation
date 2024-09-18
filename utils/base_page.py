# base_page.py

from selenium import webdriver
from config.config import Config



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        # Método para abrir cualquier URL
        self.driver.get(url)

    def quit(self):
        # Método para cerrar el navegador
        self.driver.quit()
