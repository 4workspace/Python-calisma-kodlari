# Selenium bir web otomasyonudur. Bizim yerimize belirttiğimiz bir web sitesine gidip istediğimiz etkileşimi sağlar.
# örneğin Youtube'a gidip giriş yapabilir.
# web botu yapılabilir.

# hangi tarayıcı ile çalışacaksak o tarayıcıya ait driver kullanmamız lazım. 
# Chrome için selenium-python web sitesinden ilgili driveri indirmek gerekiyor

from selenium import webdriver
import time

driver = webdriver.Chrome()                 # Firefox tarayıcısı için webdriver.Firefox() yazılmalı
url = "https://www.huobi.com/tr-tr/exchange/eth_usdt/"         #ziyaret edilecek web sitesi
driver.get(url)

time.sleep(1)                               # 2 sn bekle
driver.maximize_window()
driver.save_screenshot("huobi-website.png")
print(driver.title)
time.sleep(1)

url = "https://github.com/CSD-1993"             # gideceği bir sonra ki sayfa
driver.get(url)
print(driver.title)

time.sleep(2)
driver.back()               #önce ki sayfaya geri döner

print(driver.title)
# driver.close                                # tarayıcıyı kapat