from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver, base_url='http://www.testyou.in'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_element(self, *locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
    
    def click_element(*element):
        element.click()
