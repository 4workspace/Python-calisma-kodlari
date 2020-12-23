# parametre almayan fonksiyon
def hey():
    print('Hello')

# parametre alan, parametre almadığında da user kelimesini aldığını varsayar
def sayHello(name = 'user'):
    print('Hello ' + name)

def total(num1, num2):
    return num1 + num2

al = total(10,20)
print(al)

def bilgi():
    '''
    Bu kisimda bu sekilde notlar ekleyebilirsin
    fonksiyonu calistirdiginda
    bu sekilde yazi gorulur
    '''

print(help(bilgi))      # bu sekilde açıklamaları görebilirsin


def add(a,b,c=0):
    return sum((a,b,c))         
print(add(10,20,3))             # bu şekilde en fazla 3 en az 2 parametre girebiliriz


def add1(*parametreler):        # tek * parametreler' e gelecek olan bir 'tuple' olduğunu belirtir
    print(type(parametreler))
    return sum((parametreler)) 

print(add1(12,20,30,40))        # bu şekilde ise istediğimiz kadar parametre atayabiliriz

#********************************************************************************************************

def displayUser(**parametreler):        # burada ** (iki yıldız) ifadesi, parametreler'e dictionary listesi geleceğini belirtir {'dict': 10}
    print(type(parametreler))
    for key, value in parametreler.items():
        print('{} is {}'.format(key, value))

displayUser(name = 'Ahmet', age = 27, city = 'Ankara')          # kaç parametre geleceği önemli değil, yukarıda dictionary olarak tanımladığımız için parametre sayısı önemli değil

# şimdik ise hem normal parametre hem tuple hemde dictionary alabilen fonksiyon yazalım
def myFunc(a, b, *tuple1, **dict1):
    print(a)
    print(b)
    print(tuple1)
    print(dict1)

myFunc(10,20,30, 40, 50, 60, deneme1  = 'Ahmet', deneme2 = 'Çetin')     # a = 10, b = 20, tuple1 = (30, 40, 50, 60), dict1 = {'deneme1': 'Ahmet', 'deneme2': 'Çetin'} karşılık gelir
