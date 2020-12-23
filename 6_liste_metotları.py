numbers = [1,12,15,45,21,32,85,100]      #listeler köşeli parantez ile gösterilir
letters = ['a',"b","c","d","f","g","m","h","y","z","l"]

result = min(numbers)
result = max(numbers)

result = min(letters)
result = max(letters)

# numbers.append(50)      # en sona 50 eklendi
# numbers.insert(2,27)    # 2. indekse 27 eklendi

# numbers.pop()       # en son da ki eleman silindi
# numbers.pop(1)          # 1. indekste ki eleman silindi
# numbers.remove(100)     # 100 ü arar ve siler

numbers.sort()      # aritmetik olrak sıralandı
letters.sort()      # alfabetik olarak sıralar

letters.clear()     # bütün elmanları siler

print(letters)