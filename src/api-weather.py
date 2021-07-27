import requests
import json


# enter your api key
apikey = "06d37477eab202b26fc7cc289b12005b"
# enter locations
# cities = ["Seoul,KR", "New York,US"]
cities = ["London"]
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

# kelvin to celsius (convert the temperature unit)
k2c = lambda k: k - 273.15

for city_name in cities:
    url = api.format(city=city_name, key=apikey)
    r = requests.get(url)
    data = json.loads(r.text)

    print(data)

# 참고 : API key 생성 후에 10분정도 기다려야 valid 됨
