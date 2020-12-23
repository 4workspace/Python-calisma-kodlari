sayilar = [1,3,5,7,9,12,19,21]

# 1-hangi sayılar 3 ün katı
# for n in sayilar:
#     if(n%3 == 0):
#         print(f'{n} sayisi 3 ün katıdır.')

# 2- sayilar listesinde ki sayıların toplamı
# n = 0
# for x in sayilar:
#     n += x
# print(f"{sayilar} Sayılarının toplamı = {n}")

# 3- listede ki tek sayılarının karesi
# for n in sayilar:
#     if (n%2 != 0):
#         print(f"{n} sayinin karesi = {n**2}")

sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

# 4- şehirlerden hangisi en fazla 5 karakterlidir
# for n in sehirler:
#     leng = len(n)
#     if leng <= 5:
#         print(n)

urunler = [
    {'name':'samsung s6','price':'3000'},
    {'name':'samsung s7','price':'4000'},
    {'name':'samsung s8','price':'5000'},
    {'name':'samsung s9','price':'6000'},
    {'name':'samsung s10','price':'7000'}    
]

# 5- ürünlrin fiyat toplamı
# toplam = 0
# for a in urunler:
#     toplam += int(a['price'])
# print(toplam)

# 6- ürün fiyatı en fazla 5000 olan ürünler
for n in urunler:
    if(int(n['price']) <= 5000):
        print(n['name'])