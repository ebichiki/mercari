from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#売上履歴
URL = "https://www.mercari.com/jp/mypage/sales/histories/"
#現在使っているプロファイルへのパス
PROFILE_PATH = "/Users/username/Library/Application Support/Google/Chrome/"

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + PROFILE_PATH)

# ブラウザを開く。
driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)

# Webページにアクセス
driver.get(URL)

# 3秒待つ。
sleep(3)

# 売上履歴の要素をクラス名で取得
links = driver.find_elements_by_class_name('mypage-item-link')
for link in links:
    print(link.text)

# ブラウザを終了する。
driver.close()