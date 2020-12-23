import requests
import json

api_url = 'https://api.exchangeratesapi.io/latest?base='                # "https://exchangeratesapi.io/" web sitesinden alindi

bozulan_doviz = input("Bozulan döviz türü: ")
alinan_doviz = input("alınan doviz türü: ")
miktar = int(input(f"ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

result = requests.get(api_url + bozulan_doviz)
result = json.loads(result.text)                        # result'u json bilgiye loads ile dönüştürüyoruz

print("1 {0} = {1} {2}".format(bozulan_doviz, result["rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, result["rates"][alinan_doviz]*miktar, alinan_doviz))