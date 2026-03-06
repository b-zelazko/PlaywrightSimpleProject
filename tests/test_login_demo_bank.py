import pytest

class TestLoginDemoBank:

    def test_successful_login(self, page):
        """Successful login with correct credentials"""
        page.goto("https://demo-bank.vercel.app/")
        page.get_by_test_id("login-input").fill("Tester01")
        page.get_by_test_id("password-input").fill("Pass0000")
        page.get_by_test_id("login-button").click()

        assert page.get_by_test_id("user-name").inner_text() == "Jan Demobankowy"