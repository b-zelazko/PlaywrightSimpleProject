import pytest

class TestLoginDemoBank:
    BASE_URL = "https://demo-bank.vercel.app/"

    def test_successful_login(self, page):
        """Successful login with correct credentials"""
        page.goto(self.BASE_URL)
        page.get_by_test_id("login-input").fill("Tester01")
        page.get_by_test_id("password-input").fill("Pass0000")
        page.get_by_test_id("login-button").click()

        assert page.get_by_test_id("user-name").inner_text() == "Jan Demobankowy"


    def test_login_with_short_username(self, page):
        """Unsuccessful login with too short username"""
        page.goto(self.BASE_URL)
        page.get_by_test_id("login-input").fill("tester")
        page.get_by_test_id("login-input").blur()

        assert page.get_by_test_id("error-login-id").inner_text() == "identyfikator ma min. 8 znaków"


    def test_login_with_short_password(self, page):
        """Unsuccessful login with too short password"""
        page.goto(self.BASE_URL)
        page.get_by_test_id("login-input").fill("Tester01")
        page.get_by_test_id("password-input").fill("123456")
        page.get_by_test_id("password-input").blur()

        assert page.get_by_test_id("error-login-password").inner_text() == "hasło ma min. 8 znaków"