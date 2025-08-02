from playwright.sync_api from playwright.sync_api import sync_playwright

def run_browser(email, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # ← تم التعديل هنا
        page = browser.new_page()

        page.goto("https://app.eobroker.com/")
        page.fill('input[type="email"]', email)
        page.fill('input[type="password"]', password)
        page.click('button:has-text("تسجيل الدخول")')

        page.wait_for_timeout(10000)  # انتظر 10 ثواني بعد تسجيل الدخول
        print("✅ تم تسجيل الدخول بنجاح")
        
        # هنا تقدر تضيف أي تحليل أو توصيات لاحقًا

        browser.close()
