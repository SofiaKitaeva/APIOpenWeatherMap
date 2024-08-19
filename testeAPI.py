import requests

api_key= "38589300af199db56c0b4061f6ef7757"

lat = input("Latitude: ")
lon = input("Longitude: ")

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid='+ api_key

response = requests.get(url)

data = response.json()

clima = data["weather"]
temp = data["main"]
vento = data["wind"]

print(data)

