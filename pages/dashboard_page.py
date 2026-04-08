class DashboardPage:

    def __init__(self, page):
        self.page = page

    def make_transfer(self, receiver, amount, title):
        self.page.locator("#widget_1_transfer_receiver").select_option(receiver)
        self.page.locator("#widget_1_transfer_amount").fill(amount)
        self.page.locator("#widget_1_transfer_title").fill(title)
        self.page.get_by_role("button", name="wykonaj").click()
        self.page.get_by_test_id("close-button").click()

    def mobile_top_up(self, receiver, amount):
        self.page.locator("#widget_1_topup_receiver").select_option(receiver)
        self.page.locator("#widget_1_topup_amount").fill(amount)
        self.page.locator("#uniform-widget_1_topup_agreement > span").click()
        self.page.get_by_role("button", name="doładuj telefon").click()
        self.page.get_by_test_id("close-button").click()

    # --- GETTERS ---

    def get_message(self):
        return self.page.get_by_test_id("message-text").inner_text()

    def get_balance(self):
        return float(self.page.locator("#money_value").inner_text())