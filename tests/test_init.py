import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestInit(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    def tearDown(self) -> None: self.driver.quit()
