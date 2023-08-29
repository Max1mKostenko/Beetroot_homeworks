from requests import get

url = "https://api.openweathermap.org/data/2.5/weather?lat=50.45&lon=30.52&appid=de114f0e52203503b5b84a8c89f994ec"
_json = get(url).json()
degrees_celsius = round(_json["main"]["temp"] - 273.15, 2)
print(f'Kiev: {degrees_celsius}°C')
