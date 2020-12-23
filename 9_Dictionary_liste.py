"""
plakalar = {"Kocaeli" : 41, "İstanbul" : 34, "Ankara" : 6, "Mardin" : 47}

print(plakalar["Mardin"])

plakalar["Kayseri"] = 38            # Dic'e ekleme yapılabilir

print(plakalar)

"""
users = {
    "AhmetCetin" : {
        "Age":27, 
        "email":"ahmetcetin.eem@gmail.com",
        "Şehir":"Ankara",
        "Cep":123456
        },
    "Barta" : {
        "Age":25,
        "roles":["Yönetici","CEO"],
        "email":"adwentures.7@gmail.com",
        "Şehir":"Mardin",
        "Cep":147852
    }
}

print(users["AhmetCetin"])
print(users["AhmetCetin"]["Age"])
print(users["AhmetCetin"]["email"])
print(users["AhmetCetin"]["Şehir"])
print(users["AhmetCetin"]["Cep"])

print("")

print(users["Barta"])
print(users["Barta"]["Age"])
print(users["Barta"]["roles"])
print(users["Barta"]["roles"][0])
print(users["Barta"]["email"])
print(users["Barta"]["Şehir"])
print(users["Barta"]["Cep"])