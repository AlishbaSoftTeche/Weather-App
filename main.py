import requests
import json
city = input("Enter city: \n")
url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
r= requests.get(url)
wdic= json.loads(r.text)
w=wdic["current"]["temp_c"]
print(f"The current temperature in {city} is {w}°C.")
# print(r.text)


