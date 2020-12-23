# 1- Gönderilen bir kelimeyi belirten kez ekranda gösteren fonksiyonu yazın

# def goster(deger, sayi):
#     while sayi != 0:
#         sayi -= 1
#         print(deger+' '+ str(sayi + 1))

# kez = int(input('kaç kez göstersin: '))
# ne = input('hangi kelime gösterilsin: ')

# goster(ne,kez)

# 2- Kendine gönderilen sınırsız sayıda ki parametreyi bir listeye çeviren fonksiyonu yazınız.
# def cevir(*args):       # 1 yıldız (*) sınrız sayıda demek
#    liste = []           # boş bir liste tanımlandı
#    for i in args:
#        liste.append(i)
    
#    return liste

# result = cevir(10,20,30,40,'ahmet')
# print(result)

# 3- gönderilen 2 sayı arasında ki tüm asal sayıları bulun
'''
def asal(say1, say2):
    for i in range(say1, say2+1):
        if i > 1:
            for x in range(2, i):
                if (i % x == 0):
                    break
                else:
                    print(i)
asal(72,90)
'''

# 4- kekndisine gönderilen bi sayının tam bölenlerini bir liste şeklinde döndüren fonksionu yazın

def tambolen(sayi):
    tamBolenListe = []
    for i in range(1, sayi):
        if (sayi % i == 0):
            tamBolenListe.append(i)
    return tamBolenListe

print(tambolen(100))
