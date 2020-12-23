name = ''   # name herhandi bir string veya karakter almadığı için False olur
while not name:     # name: False, not name: True
    name = input("isminigi girin:")     # name herhangi bir değer aldığında True olur ve not name ise False olur, whilden çıkılır

print(f'Merhaba, {name}')

while not name.split():     # .split() ise booşluk karakterini baştan ve sondan siler 
    name = input("isminigi girin:")     # name herhangi bir değer aldığında True olur ve not name ise False olur, whilden çıkılır

print(f'Merhaba, {name}')