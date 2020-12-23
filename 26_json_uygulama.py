# json demo uygulama
# json bir veri depolama ve farklı platormlar arasında kullanmak içindir. Daha önceleri xml veri tipi kullanılrdı
# Bu uygulama username, password ve email kayıt yaparak kullanıcı girişi sğlar ve verileri json verisine depolar. 03.12.2020 Ahmet Çetin



import json
import os
 
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:                   # repository: Ambar, depolayıcı     
    def __init__(self):
        self.users = []                 # userları depolamak için bir liste
        self.isLoggedIn = False         # varsayılan olarak giris yapmamıs sayılıyor
        self.currentUser = {}           # giris yapan kullanıcıların bilgilerini depolamak icin dict tanımlanıyor

        # load users from .json file
        self.loadUsers()

    # kullancı bilgileri görüntüleme
    def loadUsers(self):
        if os.path.exists('users.json'):            # users.json dosyasının var olup olmadığını kontrol ediliyor
            with open('users.json', 'r', encoding = 'utf-8') as file:           # kullanıcı bilgileri okunuyor
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
            print(self.users)


        else:
            print('users adında ki dosya bulunamadı!')
    

    # kullanıcı ilgileri kaydetme
    def register(self, user: User):                 
        self.users.append(user)
        self.saveToFile()
        print('Kullanıcı olusturuldu.')

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
               self.isLoggedIn = True
               self.currentUser = user
               print('Giriş başarılı.')
               print('\nHoş geldiniz {} bey'.format(username))
               break

            else:
                print('Kulanıcı adı veya parola hatalı!')
                

    def logout(self):
        if self.isLoggedIn == False:
            print('Giriş zaten yapılmamış')
        else:
            self.isLoggedIn = False
            self.currentUser = {}
            print('Çıkış yapıldı..')

    def identity(self):
        if self.isLoggedIn == True:
            print('username: {}'.format(self.currentUser.username))
        else:
            print('Giriş yapmadınız!!!')
    
    # kullanıcı ilgileri dosyaya kaydetme
    def saveToFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))      # user class'ını (icinde ki bilgileri) bir dict'e yani sözlük verisine çeviriyor. (NOT: dump ve dumps ayrı şeyler)
        
        with open('users.json','w') as file:
            json.dump(list, file)                       # dump ile file içinde ki ilgiler list'e ekleniyor

repository = UserRepository()                            # repository = depo, kaynak, mahzen


while True:
    print("Menü".center(50, '*'))          # menü yazar ve 50 karakter (* karakteri) ortasında ortalar
    secim = input('1- Register\n2- Login\n3- Logout\n4- identity\n5- Exit\n\nSeciminiz:')

    if secim == '5':
        print('\nCikis yaptiniz...')
        break

    else:
        if secim == '1':                    #register
            username = input('Username: ')
            password = input('Password: ')
            email = input('email: ')

            user = User(username = username, password = password, email = email)
            repository.register(user)

            
            
        elif secim == '2':                  # login
             if repository.isLoggedIn:
                print('Zaten giriş yaptınız {} bey'.format(repository.currentUser.username))
                
             else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username, password)


        elif secim == '3':                  # logout
            repository.logout()

        elif secim == '4':                  #identity
            repository.identity()

        else:
            print('Yanlis secim!')
