# # // -> kalansız bölme için
# x=10
# y=4
# print(x//y)  #çıktı: 2

# # ** -> kuvveti için
# x=3
# y=2
# result = x**y #-> x üzeri y
# print(result) # çıktı: 9



x, y, z = 5, 12, 13     # x = 5, y = 12, z = 13

values = 1, 2, 3, 4, 5
print(type(values))         # type of values is tuple

# x, y, z = values        # hata! 4 ve 5 gidecek bir yer yok
# values2 = 1, 2
# x, y, z = values2           # hata, z ye eleman atanmadı

x, y, *z = values

print(x, y, z)              # output: 1 2 [3, 4, 5]
