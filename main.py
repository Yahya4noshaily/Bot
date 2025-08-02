from browser import run_browser

# بيانات تسجيل الدخول
email = "Nushily4@gmail.com"
password = "Ya12345678"
market = "smarty"        # تقدر تغيّره إلى أي سوق آخر
duration = 30            # المدة بالثواني للبقاء على الشارت

# تشغيل المتصفح والتحليل
run_browser(email, password, market, duration)
