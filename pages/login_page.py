class LoginPage:

    def __init__(self, page):
        self.page = page
        self.url = "https://demo-bank.vercel.app/"

        # locators
        self.login_input = page.get_by_test_id("login-input")
        self.password_input = page.get_by_test_id("password-input")
        self.login_button = page.get_by_test_id("login-button")

        self.error_login = page.get_by_test_id("error-login-id")
        self.error_password = page.get_by_test_id("error-login-password")
        self.user_name = page.get_by_test_id("user-name")

    def open(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.login_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()