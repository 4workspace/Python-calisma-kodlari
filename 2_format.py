"""
Burada  süslü parantez {} yerine format icine yazilan deger gelir
süslü parantezin içine ilkine 0 diğerine 1 yazıldığında sıralı şekilde yerleştirilir
ancak {} içine 1 ve 0 yazıldığında 2. yazı ilkinin yerine 1. yazı ise ikinciinin yerine yazılır
"""

name = "Ahmet"
surname = "CETIN"
age = 27

"""
print("My name is {} {}".format(name, surname))
print("My name is {0} {1}".format(name, surname))
print("My name is {1} {0}".format(name, surname))
print("My name is {n} {s}".format(n=name, s=surname))
print("My name is {s} {n}".format(n=name, s=surname))
print("My name is {n} {s}".format(n=name, s=surname))
print("My name is {} {} and I'm {} years old".format(name, surname, age))
"""
print(f"My name is {name} {surname} and I'm {age} years old")                       # bu da aynı görevi gören "f string" metodu

result = 200/700

print("the result is {}".format(result))
print("the result is {r:1.3}".format(r=result))     # 1: virgulden onceki, 3 ise virgülden sonra kaç karakterlik yer ayrılacağını belirtir
