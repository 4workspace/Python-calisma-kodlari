# list: [] ile gösterilir.
# tuple: () ile gösterilir.
# set: ([]) ile gösterilir.
# dictionary: {} ile gösterilir.

list1 = ["Python","C/C++","C#"]
list1[0] = "Artifical"              # eleman değiştirilebilir.
print(list1)

tuple1 = ("Python","C/C++","C#")
# tuple1[0] = "Artificial"              # tuple da eleman değiştirilemez.
tuple1 = ("Matlab","Simulink","Qt")   # tuple da sıfırdan eleman atanabilir     
print(tuple1)

set1 = set(["Python","C/C++","C#"])         # set'te elemanlar karışık dizlir. Her derleme de sıraları değişir
# set1[0] = "Artificial"        # set'te eleman değiştirilemez
set1 = set(["Matlab","Simulink","Qt","Qt"])     # set bildiğimiz kümeler konusu bu yüzden bir kümede aynı eleman 1 kere bulunabilir. Fazla Qt yazılmaz
print(set1)


dict1 = {1:"Python", 2:"C/C++", 3:"C#"}
dict1[0] = "Artificial" 
print(dict1 )


print(type(list1))
print(type(tuple1))
print(type(set1))
print(type(dict1))