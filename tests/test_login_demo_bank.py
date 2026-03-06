import pytest

class TestLoginDemoBank:
    BASE_URL = "https://demo-bank.vercel.app/"

    def test_successful_login(self, page):
        """Successful login with correct credentials"""

        # Arrange
        username = "Tester01"
        password = "Pass0000"
        page.goto(self.BASE_URL)

        #Act
        page.get_by_test_id("login-input").fill(username)
        page.get_by_test_id("password-input").fill(password)
        page.get_by_test_id("login-button").click()

        #Assert
        assert page.get_by_test_id("user-name").inner_text() == "Jan Demobankowy"


    def test_login_with_short_username(self, page):
        """Unsuccessful login with too short username"""

        #Arrange
        username = "Tester"
        page.goto(self.BASE_URL)

        #Act
        page.get_by_test_id("login-input").fill(username)
        page.get_by_test_id("login-input").blur()

        #Assert
        assert page.get_by_test_id("error-login-id").inner_text() == "identyfikator ma min. 8 znaków"


    def test_login_with_short_password(self, page):
        """Unsuccessful login with too short password"""

        #Arrange
        password = "Pass"
        username = "Tester01"
        page.goto(self.BASE_URL)

        #Act
        page.get_by_test_id("login-input").fill(username)
        page.get_by_test_id("password-input").fill(password)
        page.get_by_test_id("password-input").blur()

        #Assert
        assert page.get_by_test_id("error-login-password").inner_text() == "hasło ma min. 8 znaków"