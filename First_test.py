from playwright.sync_api import sync_playwright

def test_open_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.google.com")
        assert "Google" in page.title()

        print("Browser Launch successfully!")

        page.wait_for_timeout(5000)  # keep browser open for 5 sec
        browser.close()

if __name__ == "__main__":
    test_open_google()
