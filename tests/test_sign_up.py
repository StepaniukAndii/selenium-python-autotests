from pages.pages import SignUpPage
from tests.test_init import TestInit


class SingUpTest(TestInit):

    def test_sign_up_validation_password(self):
        page = SignUpPage(self.driver)
        page.open()
        page.registration('', 'andi@gmail.com', '1234842784', '12345', '12345', '123')
        self.assertEqual(len(page.get_error()), 1)

    def test_sign_up_validation_email(self):
        page = SignUpPage(self.driver)
        page.open()
        page.registration('andi', '', '1234842784', '12345', '12345', '123')
        self.assertEqual(len(page.get_error()), 1)

    def test_sign_up_validation(self):
        page = SignUpPage(self.driver)
        page.open()
        page.click_submit()
        self.assertEqual(len(page.get_error()), 6)

    def test_sign_up_validation_word(self):
        page = SignUpPage(self.driver)
        page.open()
        page.registration('Andrii', 'andi@gmail.com', '1234842784', '12345', '12345', '123')
        self.assertEqual(page.get_error_valid().text, 'Invalid Code!')
