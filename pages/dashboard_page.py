class DashboardPage:

    def __init__(self, page):
        self.page = page

    def make_transfer(self, receiver, amount, title):
        self.page.locator("#widget_1_transfer_receiver").select_option(receiver)
        self.page.locator("#widget_1_transfer_amount").fill(amount)
        self.page.locator("#widget_1_transfer_title").fill(title)
        self.page.get_by_role("button", name="wykonaj").click()
        self.page.get_by_test_id("close-button").click()

    def get_message(self):
        return self.page.get_by_test_id("message-text").inner_text()