import json
import requests

url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = 'c56acbeaaca5e2d687e40deac85f750e'
print("Enter your city name of which you want to know weather forecast")
city = input()

combined_URL = url + "q="+city + "&appid="+api_key

mapValue = {
     
}


responce = requests.get(combined_URL)

res=responce.json()
#print(json.dumps(responce.json())) #>>> For better viewing of json value
if(res['cod']!=401):
    print(f"Featching data ...........\n The weather update of {city} is ...")
    
    main = res['main']
    Current_Temperature= main['temp']
    feels_like=main['feels_like']
    Pressure=main['pressure']
    Humidity=main['humidity']

    print(f"Current temperature : {(Current_Temperature-32)*0.55556} C, Feels like : {(feels_like-32)*0.55556}C \n Pressure : {Pressure} \n Humidity : {Humidity} ")

else:
    print("try again later....")
