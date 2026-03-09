from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestDashboard:

    def test_money_transfer(self, page):
        """Successful money transfer"""

        # Arrange
        login_page = LoginPage(page)
        dashboard = DashboardPage(page)

        login_page.open()
        login_page.login("testerLO", "12345678")

        # Act
        dashboard.make_transfer("2", "150", "zwrot kasy")

        # Assert
        assert dashboard.get_message() == \
            "Przelew wykonany! Chuck Demobankowy - 150,00PLN - zwrot kasy"