from playwright.sync_api import sync_playwright

def run_browser(email, password, market="smarty", duration=30):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://app.eobroker.com/")
        
        page.wait_for_timeout(3000)
        page.locator('input[name="email"]').fill(email)
        page.locator('input[name="password"]').fill(password)
        page.locator('button[type="submit"]').click()

        page.wait_for_timeout(8000)
        page.goto(f"https://app.eobroker.com/trade/otc/{market}")

        print("✅ تم الدخول للمنصة وتشغيل السوق:", market)
        page.wait_for_timeout(duration * 1000)

        browser.close()
