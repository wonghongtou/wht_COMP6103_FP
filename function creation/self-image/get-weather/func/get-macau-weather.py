import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=22.20&longitude=113.55&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
