import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
data = response.json()
print(data["value"])

kaupunki = input("Anna paikkakunnan nimi: ")
url1 = "https://api.openweathermap.org/data/2.5/weather"
api_key = "6627606b867fedfcb0068284f1c6ca83"
params1 = {"q": kaupunki, "appid": api_key, "units": "metric"}
response = requests.get(url1, params=params1)
data1 = response.json()
l = data1["main"]
l1 = l["temp"]
d = data1["weather"]
d1 = d[0]
d2 = d1["description"]
print(kaupunki)
print(f"Lämpötila: {l1}")
print("Säätila: " + d2)