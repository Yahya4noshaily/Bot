from strategies.macd_rsi_combo import analyze_macd_rsi
from strategies.support_resistance import check_support_resistance
from filters import is_volatile
import json
import asyncio
from playwright.async_api import async_playwright

async def run_bot():
    with open("config.json") as f:
        config = json.load(f)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://app.eobroker.com/trade/otc/eur-usd")

        print("📊 تم فتح منصة EO Broker...")
        await page.wait_for_timeout(5000)  # انتظر تحميل الشارت

        # تمثيل لسحب السعر من الشارت
        price = 1.23  # في الكود الحقيقي: تحليل صورة أو قراءة السعر لايف

        if not is_volatile(price):
            if analyze_macd_rsi(price) and check_support_resistance(price):
                print("✅ دخول آمن")
            else:
                print("❌ إشارة غير مؤكدة")
        else:
            print("⚠️ السوق متذبذب")

        await browser.close()

asyncio.run(run_bot())
