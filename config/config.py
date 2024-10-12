import os
import platform


class Config:
    if platform.system() == "Windows":
        CHROME_DRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../chromedriver.exe")
    elif platform.system() == "Darwin":  # MacOS
        CHROME_DRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../chromedriver")
    elif platform.system() == "Linux":
        CHROME_DRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../chromedriver")

    # URL del sitio de inicio de sesión
    BASE_URL = "https://spaceshine.shop"

    # Tiempo de espera predeterminado en segundos
    DEFAULT_WAIT_TIME = 10


