# genel kullanılan web sitesi: https://selenium-python.readthedocs.io/locating-elements.html 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # enter veya space tuşunu import etmek için
import time


driver = webdriver.Firefox()
url = "http://youtube.com"
driver.get(url)
driver.maximize_window()

searchInput = driver.find_element_by_name("search_query")           # youtube da search kısmına sağ tık ve çıkan yerde ki name etiketine karşılık gelen "search_query" alındı
time.sleep(1)
searchInput.send_keys("vusal namazli piano")            # youtube arama çubuğunda aranacak kelimeler
time.sleep(1)
searchInput.send_keys(Keys.ENTER)                       # enter yapıldı
time.sleep(1)


