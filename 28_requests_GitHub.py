import requests
import json

class GitHub:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '22fa5f7f321921a9b24a7b40a24e1dece8656cae'                 # github.com/4workspace.com'a ait test token

    def getUser(self, username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()              # girilen kullanıcıya ait json dosyası alınıyor

    def getRepository(self, username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()

    def createRepository(self, name):                                                   # "https://developer.github.com/v3/repos/#create"  web sitesinden alındı
        respons = requests.post(self.api_url + '/user/repos?access_token='+ self.token, json={    
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com/4workspace.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return respons.json()              # json bilgisi döner

github = GitHub()

while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSecim: ')

    if secim == '4':
        print('Çıkış yaptınız.')
        break

    else:
        if secim == '1':            # Find User
            username = input('Username: ')
            result = github.getUser(username)
            print(f"name: {result['name']}\npublic repos: {result['public_repos']}\nfollowers: {result['followers']}")


        elif secim == '2':          # Get Repos
            username = input('Username: ')
            result = github.getRepository(username)
            for repo in result:
                print(repo['name'])


        elif secim == '3':          # Create Repos
            name = input('repostroy name: ')
            result = github.createRepository(name)
            if result == None:
                print(f'{name} adında ki Repository oluşturulamadı!')
            else:
                print(result)
                print(f'{name} adında ki Repository oluşturuldu.')




        else:                       # Wrong choice
            print('Yanlis seçim!')