username = "username"
password = "*********"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languange':'en, en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)               # sadece bunu kullansaydık chromun varsayıln özelliklerini kullanmış olacktık, parantez içine ise yazdığımız ayarları implement ettik

        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get('https://twitter.com/login')
        usernameInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        time.sleep(1)
        self.browser.maximize_window()
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        loginButton = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div')
        loginButton.click() 
        time.sleep(2)  

twitter = Twitter(username, password)
twitter.signIn()

