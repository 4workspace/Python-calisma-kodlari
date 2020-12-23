website = "www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# Soru 1: ' Hello World ' karakter dizisinde baş ve sonda ki boşlukları silin?
message = ' Hello World '
x = message.strip()

# Soru 2: 'www.sadikturan.com' içinden sadikturan haricinde ki karakterlerini silin


# Soru 3: 'course' içinde ki tüm karakterleri küçük harf yapın
x = course.lower()

# Soru 4: 'website' içinde kaç tane a karakteri vardır? (count)
x = website.count('a')

# Soru 5: 'website' www ile başlayıp com ile bityor mu?
x = website.startswith("www")
x = website.endswith("com")

# Soru 6: 'website' içerisinde .com ifadesi var mı?
# x = website.isinstance(".com")

# Soru 7: 'course' içinde ki hepsi alfabetik mi? (isalpha, isdigit)
x = course.isalpha()

# Soru 8: 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağına ve soluna * ekleyiniz.
message = "Contents"
x = message.center(50, "*")

# Soru 9: 'course' içinde kii tüm boşlukları '--' ile doldurun
x = course.replace(" ", "--")

# Soru 10: 'Hello World' içinde ki World'u There ile değiştirin
message = "Hello World"
x = message.replace("World","There")

# Soru 11: 'course' karakter dizisini boşluk karakterlerinden ayırın
x = course.split(" ")



print(x)