# greeting = 'Hello There'
# index = 0
# for letter in greeting:
#     print(f'index: {index} letter: {letter}')
#     index += 1

# enumerate kullanırsak
# for item in enumerate(greeting):
#     print(item)
    

# enumerate yi indexlerine  ayırırsak
# for index, letter in enumerate(greeting):
#     print(f'index: {index} letter: {letter}')

# zip

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
# liset1 ve liste2 yi birbirine bağlayacağız yani liste1, liste2 nin indexleri yapacağız
# list = list(zip(list1, list2))   # list( ) ile listeye çevirip list'e attık
# print(list)

list3 = [100,200,300,400,500]  #gibi 3. liste de eklenebilir
list = list(zip(list1, list2, list3))
print(list)