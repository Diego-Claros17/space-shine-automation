import os


class Config:
    # Ruta hacia el driver de Google Chrome
    CHROME_DRIVER_PATH = CHROME_DRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../chromedriver.exe")   # Asegúrate de colocar la ruta correcta en tu sistema

    # URL del sitio de inicio de sesión
    LOGIN_URL = "https://b1h24fidf8ia0a73-89346277698.shopifypreview.com"
# Tiempo de espera predeterminado en segundos
    DEFAULT_WAIT_TIME = 10