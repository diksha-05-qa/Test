from playwright.sync_api import sync_playwright

def test_open_orangehrm():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Validate page title
        assert "OrangeHRM" in page.title()

        print("OrangeHRM Login page launched successfully!")

        page.wait_for_timeout(5000)
        browser.close()

if __name__ == "__main__":
    test_open_orangehrm()
