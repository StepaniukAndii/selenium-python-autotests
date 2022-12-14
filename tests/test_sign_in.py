from pages.pages import HomePage, LoginPage
from tests.test_init import TestInit


class TestSignIn(TestInit):

    def test_page_load(self):
        page = HomePage(self.driver)
        page.open()
        self.assertTrue(page.check_page_loaded())

    def test_login_validation(self):
        page = LoginPage(self.driver)
        page.open()
        page.login("and@gmail.com", "12345")
        self.assertEqual(page.getErrorMessage(), "Userid or Password did Not Match !!")

    def test_login_validation_email(self):
        page = LoginPage(self.driver)
        page.open()
        page.login("", "12345")
        self.assertEqual(page.getErrorMessage(), "Userid or Password did Not Match !!")

    def test_login_validation_password(self):
        page = LoginPage(self.driver)
        page.open()
        page.login("and@gmail.com", "")
        self.assertEqual(page.getErrorMessage(), "Userid or Password did Not Match !!")

    def test_forgot_password(self):
        page = LoginPage(self.driver)
        page.open()
        page.click_forgot_password()
        self.assertEqual(self.driver.current_url, "http://testyou.in/ForgetPassword.aspx")

    def test_sign_up_link(self):
        page = LoginPage(self.driver)
        page.open()
        page.click_sign_up_link()
        self.assertEqual(self.driver.current_url, "http://www.testyou.in/SignUp.aspx")