import requests
#import androidhelper as android

#def get_coordinates():
#    droid = android.Android()
#    location = droid.readLocation().result
#    if location is not None:
#        gps = location["gps"]
#        coord = gps["latitude"]
#        coord.append(gps["longitude"])
#        return location
#    else:
#        return None


api_key= "38589300af199db56c0b4061f6ef7757"

#c = get_coordinates()
#print(c)

#if c is not None:
#   lat, lon = c
#else:
#   print("Unable to retrieve your GPS coordinates.")

lat = input("Latitude: ")
lon = input("Longitude: ")

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid='+ api_key

response = requests.get(url)

data = response.json()
clima = data["weather"]
temp = data["main"]
vento = data["wind"]

print(data)

