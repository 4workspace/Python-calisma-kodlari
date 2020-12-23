website = "https://www.sadikturan.com/"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# Soru 1: 'course' karakter dizisinde kaç karakter olduğunu bulunmaktadır?
print("'course' karakter sayisi {} \n" .format(len(course)))

# Soru 2: 'website' içinden www karakterlerini alın
print("Alinan karakgterler {} \n".format(website[8:11]))

# Soru 3: 'website' içinden com karakterlerini alın
print("Alinan karakgterler {} \n".format(website[-4:-1]))

# Soru 5: 'course' içinden ilk 15 ve son 15 karakterlerini alın
print("ilk 15 karakter: " + course[:15] + "   ve   Son 15 karakter: " + course[-15:] + "\n")

# Soru 5: 'course' ifadesinde ki karakterlerin tersten yazdırın
print(course[::-1] + "\n")


# name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'
# Soru 6: Yukarıda ki değişkenler ile ekrana aşağıda ki şu ifadeyi yazdırın
# 'benim adım Bora Yılmaz, Yaşım 32 ve meskeğim mühendis.'
name = "Bora"
surname = "Yılmaz"
age = 32
job = "mühendis"
print(f"Benim adım {name} {surname}, Yaşım {age} ve meskeğim {job}. \n")

# Soru 7: 'Hello world' ifaddesinde ki w harfini 'W' ile değiştirin
m = "Hello world"
print(m.replace('w','W')) 
s = m[:6] + "W" + m[7:]                             # bu şekilde de yazılabilir
print(s)

# Soru 8: 'abc' ifadesinii yan yana 3 defa yazdırın
print("abc"*3)