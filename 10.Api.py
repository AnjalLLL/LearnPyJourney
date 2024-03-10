import requests

url = "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
api_key = "c56acbeaaca5e2d687e40deac85f750e"
print("Enter your city name of which you want to know weather forecast")
city = input()

combined_URL = url + "q="+city + "&appid="+api_key


responce = requests.get(combined_URL)

res=print(responce.text)
if(res['cod']!=401):
    print("Featching data ...........\n The weather update of {city} is ...\n")
    print(f"Temperature : {res['temp']} \n Humidity : {res['humidity']} \n Pressure : {res['pressure']} ")
else:
    print("try again later....")
