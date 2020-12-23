x = 25

def changeX(x):
    x = 50

changeX(x)
print(x)        # x global olduğu için fonksiyonun içinde değiştirilemedi

y = 100
def changeY():
    global y
    y = 150

print(f'Fonksiyondan önce y:{y}')
changeY()
print(f'Fonksiyondan sonra y:{y}')