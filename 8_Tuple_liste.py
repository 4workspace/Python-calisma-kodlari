# liste de listeye eleman eklenebilir veya değiştirilebilir
# tuple da eleman değişim mümkün değil ama sıfırdan bir liste atanabilir

liste = [1, "Cetin", 25, 5.8]
Tuple = (1, "Cetin", 2, 5.8)

print(type(liste))
print(type(Tuple))

print(liste[1])
print(Tuple[1])

liste = liste + ["Benane"]
Tuple = ("Ankara", "Istanbul")      #doğru
# Tuple = Tuple + ("Bardo")   hatalı
print(liste)
print(Tuple)