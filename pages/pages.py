from pages.base_page import BasePage
from utils.locators import HomePageLocators, RegistrationLocators
from utils.locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)

    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.locator.SUBMIT).click_element()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def getErrorMessage(self):
        return self.find_element(*self.locator.ERROR_MESSAGE).text

    def open(self):
        self.driver.get("http://www.testyou.in/Login.aspx")
        return LoginPage

    def click_forgot_password(self):
        self.find_element(*self.locator.FORGOT_PASSWORD).click()

    def click_sign_up_link(self):
        self.find_element(*self.locator.SIGN_UP_LINK).click()


class HomePage(BasePage):
    def __init__(self, driver, base_url='http://www.testyou.in'):
        super().__init__(driver, base_url)
        self.locator = HomePageLocators

    def open(self):
        self.driver.get("http://demo.testyou.in/")
        self.wait_element(*self.locator.LOGO)

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False


class SignUpPage(BasePage):
    def __init__(self, driver, base_url='http://www.testyou.in'):
        super().__init__(driver, base_url)
        self.locator = RegistrationLocators

    def open(self):
        self.driver.get('http://www.testyou.in/SignUp.aspx')

    def registration(self, name, email, loginid, password, reEnter, word):
        self.find_element(*self.locator.NAME).send_keys(name)
        self.find_element(*self.locator.EMAIL).send_keys(email)
        self.find_element(*self.locator.LOG_ID).send_keys(loginid)
        self.find_element(*self.locator.PASSWORD).send_keys(password)
        self.find_element(*self.locator.RE_ENTER_PASSSWORD).send_keys(reEnter)
        self.find_element(*self.locator.WORD_VEREFICATION).send_keys(word)
        self.click_submit()

    def click_submit(self):
        self.find_element(*self.locator.SUBMIT).click()

    def get_error(self):
        return self.find_elements(*self.locator.ERROR_MESSAGE)

    def get_error_valid(self):
        return self.find_element(*self.locator.ERROR_MESSAGE_VALID)
