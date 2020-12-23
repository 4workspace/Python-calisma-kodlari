# OOP'da class ve object tanımı var. Class'ın içinde ise attributs ve methots bulunur
'''
*p1 ve p2 objesi tanımlandı ve p1 veya p2 objesi üzerinden Person class'ı üzerinden tanımlanan attributs ve
methodlara ulaşılabilir
*self'in anlamı class tan türetilmiş herhangi bir objeyi( p1,p2) temsil eder
*p1 veya p2 üzerine herhangi bir değer aktarmak için 'self' kullanılır. Bu değer ise name ve year olarak
tanımlanabilir

'''

# 1- class
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
    
    # methods


# 2- object (instance)
p1 = Person('Ahmet', 1992)                   
p2 = Person(name = 'A', year = 20)      # bu şeklde de yapılabilir.

print(p1)
print(f'isim: {p1.isim}, yıl: {p1.yil}, adres bilgisi: {p1.adres}')

# Bilgi güncelleme
p1.isim = 'Artifical'
p1.yil = 30
p1.adres = 'Ankara'
print(f'isim: {p1.isim}, yıl: {p1.yil}, adres bilgisi: {p1.adres}')


