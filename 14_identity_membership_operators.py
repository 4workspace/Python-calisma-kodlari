# Identity Operatörü: is (referans karşılatırması yapar)
x = y = [1, 2, 3]       # x ve y aynı değere ve referansa sahip
z = [1, 2, 3]

print(x==y)     # True, değerler aynı
print(x==z)     # True, değerler aynı
print(x is y)   # True, referansları aynı
print( x is z)  # False, referansları farklı
print( x is not z)  # False, referansları farklı değil (mi)




# Memebership Operatörü: in (içinde var mı? varsa True yoksa False döndürür)
x = ['apple', 'banana']
print('banana' in x)       # True döner

name = 'Çetin'
print('e' in name)      # True