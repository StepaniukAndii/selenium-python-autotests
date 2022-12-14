from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    EMAIL = (By.CSS_SELECTOR, '#ctl00_CPHContainer_txtUserLogin')
    PASSWORD = (By.CSS_SELECTOR, '#ctl00_CPHContainer_txtPassword')
    SUBMIT = (By.CSS_SELECTOR, '[name="ctl00$CPHContainer$btnLoginn"]')
    ERROR_MESSAGE = (By.XPATH, '//*[@id="ctl00_CPHContainer_lblOutput"]')
    FORGOT_PASSWORD = (By.CSS_SELECTOR, '#ctl00_CPHContainer_hprlnkForgetPassword')
    SIGN_UP_LINK = (By.XPATH, '(//*[@class="signup_link"]/a)[2]')


class HomePageLocators(object):
    LOGO = (By.XPATH, '//*[@class="grid_7 logo "]')


class RegistrationLocators(object):
    EMAIL = (By.CSS_SELECTOR, '#ctl00_CPHContainer_txtEmail')
    PASSWORD = (By.CSS_SELECTOR, '#ctl00_CPHContainer_txtpassword')
    SUBMIT = (By.CSS_SELECTOR, '[name="ctl00$CPHContainer$btnRegistration"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '#ctl00_CPHContainer_valsAll > ul > li')
    NAME = (By.CSS_SELECTOR, '#ctl00_CPHContainer_txtFname')
    LOG_ID = (By.CSS_SELECTOR, '#ctl00_CPHContainer_txtUserLogin1')
    RE_ENTER_PASSSWORD = (By.CSS_SELECTOR, '#ctl00_CPHContainer_txtReType')
    WORD_VEREFICATION = (By.CSS_SELECTOR, '#ctl00_CPHContainer_txtVarificationCode')
    ERROR_MESSAGE_VALID =(By.CSS_SELECTOR, '#ctl00_CPHContainer_lblResult')