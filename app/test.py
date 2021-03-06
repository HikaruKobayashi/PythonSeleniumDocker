# Seleniumを使用する為にモジュールをインポートする。 
import time
from time import sleep
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# あらゆる環境でSeleniumが動作する為の設定。
chrome_path = '/usr/bin/chromium-browser'
chromedriver_path = '/usr/lib/chromium/chromedriver'
o = Options()
o.binary_location = '/usr/bin/chromium-browser'
o.add_argument('--headless') # CUIで動作するように。
o.add_argument('--disable-gpu')
o.add_argument('--no-sandbox')
o.add_argument('--window-size=1200x600')
o.add_argument('--disable-desktop-notifications')
o.add_argument("--disable-extensions")
o.add_argument('--lang=ja') # 言語設定
# o.add_argument('--blink-settings=imagesEnabled=false') # 画像の読み込みを行わないことで高速化する。

# ログインに必要な情報
url = 'https://www.amazon.co.jp/'
address = ''
password = ''

# WebDriverの起動
d = webdriver.Chrome(chromedriver_path, options=o)
d.get(url) # Webページにアクセスする。　Amazon.com
time.sleep(3) # 3秒待機
# ログイン処理
d.find_element_by_xpath("//a[@id='nav-link-accountList']/span").click()
d.find_element_by_id('ap_email').send_keys(address)
d.find_element_by_xpath("//input[@id='continue']").click()
d.find_element_by_id('ap_password').send_keys(password)
d.find_element_by_id("signInSubmit").click()


# 検索窓にSeleniumと入力する
# selector = '#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input'
# element = d.find_element_by_css_selector(selector)
# element.send_keys('Python')
# enterキーを押して検索をする。
# element.send_keys(Keys.ENTER)

# 結果の画面をスクリーンショットで保存する。
d.set_window_size(1280, 720)
d.execute_script("window.scrollTo(0, 600);")
d.save_screenshot('screenshot.png')

s = Service(executable_path=chromedriver_path)
s.start()
d = webdriver.Remote(
  s.service_url,
  desired_capabilities=o.to_capabilities()
)
d.get('https://www.google.com')
print(d.title)

d.quit()
