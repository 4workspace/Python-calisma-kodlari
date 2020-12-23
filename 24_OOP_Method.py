'''
class Person:
    # attributes
        # class seviyesinde (class attributes)
    adres = 'Bilgi girilmedi'
        # object attributes, constructor (yapıcı metot) içerisinde tanımlanır
    def __init__(self, name, year):         
        # object attributes seviyesinde attributs tanımlanır
            self.isim = name
            self.yil = year
            print('init methodu çalıştı')
    
    # instannce methods
    def intro(self):
        print('Hello there. I am ' + self.isim + ' and year is ' +  str(self.yil))

    def calculate(self):
        return 2020 - self.yil          # self.yil == p1.yil

p1 = Person(name = 'Ahmet', year = 1992)
p1.intro()
print(p1.calculate())
print(f'Adım: {p1.isim} ve yaşım: {p1.calculate()}')
'''

'''--------------------------------------------------------------------------------------------------------'''

class Circle():
    # Class object attributes
    pi = 3.1415

    def __init__(self, yaricap = 1):            # yariçap bilgisi gelmezse 1 alınır
        self.yaricap = yaricap                  # burada self.x de yazılabilir, onemli olan sağda ki ifade ile bir üstünde parantezde tanımlananın aynı olması

    # Methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap           # çemberin çevresi: 2.pi.r

    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)      # çemberin alanı: pi.r^2



C1 = Circle()       # hiçbirşey yazmadık ozaman yarıçap: 1 alındı
C2 = Circle(5)      # yarıçap = 5 alındı

print(f'C1: Çemberin çevresi: {C1.cevre_hesapla()} ve alanı: {C1.alan_hesapla()}')
print(f'C2: Çemberin çevresi: {C2.cevre_hesapla()} ve alanı: {C2.alan_hesapla()}')