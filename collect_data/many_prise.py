import requests
import json


data = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/').json()


with open('result_mant_price.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
