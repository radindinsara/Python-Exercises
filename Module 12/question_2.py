import requests

api_key = "YOUR_API_KEY"
city = input("Enter municipality name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()

print(f"Weather: {data['weather'][0]['description']}")
print(f"Temperature: {data['main']['temp']} Celsius")
