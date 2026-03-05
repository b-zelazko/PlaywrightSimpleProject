from playwright.sync_api import Playwright, sync_playwright, expect


def test_login_demo_bank():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo-bank.vercel.app/")

        # Login
        page.get_by_test_id("login-input").fill("Tester01")
        page.get_by_test_id("password-input").fill("Pass0000")
        page.get_by_test_id("login-button").click()

        # Verify that the user has successfully logged in
        assert page.get_by_test_id("user-name").inner_text() == "Jan Demobankowy"

        # ---------------------
        context.close()
        browser.close()

# This ensures the test runs when executing the script directly without pytest
if __name__ == "__main__":
    test_login_demo_bank()