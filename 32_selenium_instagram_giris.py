# İnstagramda oturum açma

# email = input("Kullanıcı adı veya email girin: ")
# password = input("Şifrenizi girin: ")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = "username"
password = "password"

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/?hl=tr")
        time.sleep(1)
        self.browser.maximize_window()

        usernameInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        
        usernameInput = usernameInput.send_keys(self.username)
        passwordInput = passwordInput.send_keys(self.password)
        #passwordInput.send_keys(Keys.ENTER)                 # password kısmandayken entere basıyor
        signin = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        signin.click()                                          # giriş yap ikonu tıklanıyor

##################################### BURAYA KADAR INSTAGRAMA GIRIS ICIN ######################################################

        def getFollowers(self):
            self.browser.get(f'https://www.instagram.com/{self.username}/')
            followersLink = self.browser.find_element_by_xpath('')
            followersLink.click()


insta = Instagram(username, password)              # class'ın tüm özelliğini "insta"ya yükledik
insta.signIn()                                  # insta üzerinden signIn() metodunu çağırdık
insta.getFollowers()

