names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyin
names.append("Cenk")

# 2- "Sena" değerini listenin başına ekleyin
names.insert(0,"Sena")

# 3- "Deniz" ismini listeden siliniz
# names.remove("Deniz")

# 4- "Deniz" isminin indeksi nedir
r = names.index("Deniz")

# 5- "Ali" listenin bir elemanı mıdır
r = "Ali" in names

# 6- liste elemanlarının ters çeviriniz
r = names.reverse()
r = names[::-1]

# 7- liste elemanlarını alfabetik olarak sıralayınız
names.sort()


# 8- years listesini rakamsal büyüklüğe göre sıralayınız
years.sort(reverse = True)

# 9- str = "Chevrolet, Dacia" karakter dizisini listete çeviriniz
str = "Chevrolet, Dacia"
ra = str.split(",")
# 10- years dizisinin en büyük ve en küçük elemanı nedir
r = max(years)
r = min(years)

# 11- years dizisinin kaç tane 1998 değeri vardır
r = years.count(1998)

# 12-years dizisinin tüm elemanlarını siliniz
r = years.clear()

# 13- kullanıcıdan alacağınnız 3 tane marka bilgisini bir listede saklayınız
my_list = [] 


for i in range(0, 3):
    x = input()
    my_list.append(x)

print(my_list)

print(ra)