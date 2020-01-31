import requests
print("_____________________WEATHER STATUS APPLICATION_________________________")
city=input("Enter city-")
url="https://api.openweathermap.org/data/2.5/weather?q="+city+",india&appid=79749721eda5f3f8426b0706b0a4d919"
json_data=requests.get(url=url).json()
Temp=json_data['main']['temp']
print("Weather is:",json_data['weather'][0]['main'])
print(f"Temperature is: {Temp-273.15} C")
print("Pressure is:",json_data['main']['pressure'])
print("Humidity is:",json_data['main']['humidity'])
print("Wind Speed is:",json_data['wind']['speed'])


