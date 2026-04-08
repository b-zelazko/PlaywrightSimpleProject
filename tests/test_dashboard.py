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

    def test_successful_mobile_top_up(self, page):
        # Arrange
        login_page = LoginPage(page)
        dashboard = DashboardPage(page)

        login_page.open()
        login_page.login("testerLO", "12345678")

        # Act
        dashboard.mobile_top_up("500 xxx xxx", "100")

        # Assert
        assert dashboard.get_message() == \
            "Doładowanie wykonane! 100,00PLN na numer 500 xxx xxx"


    def test_correct_balance_after_mobile_top_up(self, page):
        # Arrange
        login_page = LoginPage(page)
        dashboard = DashboardPage(page)

        login_page.open()
        login_page.login("testerLO", "12345678")

        initial_balance = dashboard.get_balance()
        top_up_amount = 100

        # Act
        dashboard.mobile_top_up("500 xxx xxx", str(top_up_amount))

        # Assert
        assert dashboard.get_balance() == initial_balance - top_up_amount