import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage


class TestLoginDemoBank:

    def test_successful_login(self, page):
        """Successful login with correct credentials"""

        # Arrange
        login_page = LoginPage(page)
        login_page.open()

        # Act
        login_page.login("Tester01", "Pass0000")

        # Assert
        expect(login_page.user_name).to_have_text("Jan Demobankowy")


    def test_login_with_short_username(self, page):
        """Unsuccessful login with too short username"""

        # Arrange
        login_page = LoginPage(page)
        login_page.open()

        # Act
        login_page.login_input.fill("tester")
        login_page.login_input.blur()

        # Assert
        expect(login_page.error_login).to_have_text("identyfikator ma min. 8 znaków")


    def test_login_with_short_password(self, page):
        """Unsuccessful login with too short password"""

        # Arrange
        login_page = LoginPage(page)
        login_page.open()

        # Act
        login_page.login_input.fill("Tester01")
        login_page.password_input.fill("123456")
        login_page.password_input.blur()

        # Assert
        expect(login_page.error_password).to_have_text("hasło ma min. 8 znaków")