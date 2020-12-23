# 1- Kullanıcıdan isim soyisim, eğitim ve yaş bilgileri istenecek ve ehliyet alıp alamama
#     durumu kontrol edilecek. Ehliyet alma koşulu en az 18 yaş ve 
#     lise yada üniversite mezunu olmalıdır.

# isim = input("İsminiz: ")
# soyisim = input("Soyisminiz: ")
# egitim = input("Eğitimiz (ilk, orta, lise, lisans): ")
# yas = int(input("Yaşınız: "))

# if (yas >= 18) and ((egitim == "lise") or (egitim == "lisans")):
#     print(f"Tebrikler {isim} {soyisim} bey! Ehliyet alabilirsiniz")

# elif (yas < 18):
#     print(f"{isim} malesef yaşın tutmuyor bu yüzden ehliyet alamazsınız")
# elif (egitim != "lise") or (egitim != "lisans"):
#      print(f"{isim} bey malesef eğitiminiz yetersiz")
# else:
#     print(f"{isim} {soyisim} üzgünüz ehliyet alamazsınız")

# 2- Bir öğrencinin iki yazılı notu 1 sözlü otunu alıp hesaplanan ortalamaya göre
#     not aralığına karşılık gelen not bilgisisni yazdırınız.
#     0-24   => 0
#     25-44  => 1
#     45-54  => 2
#     55-69  => 3
#     70-84  => 4
#     85-100 => 5

# yazili1 = int(input("1. yazılı notu: "))
# yazili2 = int(input("2. yazılı notu: "))
# sozlu = int(input("Sozlu notu: "))

# ort = float(((yazili1 + yazili2)/2)*0.6 + sozlu*0.4)

# if ort <= 24:
#     print(f"Ortalama:{ort} ve Not değeri: 0")
# elif ort <= 44:
#     print(f"Ortalama:{ort} ve Not değeri: 1")
# elif ort <= 54:
#     print(f"Ortalama:{ort} ve Not değeri: 2")
# elif ort <= 69:
#     print(f"Ortalama:{ort} ve Not değeri: 3")
# elif ort <= 84:
#     print(f"Ortalama:{ort} ve Not değeri: 4")
# else:
#     print(f"Ortalama:{ort} ve Not değeri: 5")


# 3- Trafiğe çıkış tarihi alan bir aracın servis zamanını aşağıda ki bilgilere
#     göre hesaplayınız.
#     1. Bakım => 1. yıl
#     2. Bakım => 2. yıl
#     3. Bakım => 3. yıl
#     
#     süre hesabını alınan gün, ay, yıl bilgisine göre gün bazl hesaplayınız
    # datatime modülü kullanılmalı

import datetime

tarih = input("Aracınız hangi tarihte trafiğe çıktı: ")
tarih = tarih.split('/')        # gelen 2020/06/24 şeklinde ki tarihi / 'den ayıracağız

trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis

gun = fark.days     # verilen tarihten günü aldık sadece, kaç gün eder yani
print(f'\nAracınız {gun} gün önce trafiğe çıktı\n')

if gun <= 365:
    print("1. servis aralığı")
elif gun <= 365*2:
    print("2. servis aralığı")
elif gun <= 365*3:
    print("3. servis aralığı")
else:
    print("Hatalı tarih girdiniz")