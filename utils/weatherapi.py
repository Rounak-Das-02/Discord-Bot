import requests
import json

def weatherupdate(city):

    f = open(r".\tokens\token.json", )
    s = json.load(f)

    api_key = s["WeatherApi"]

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(complete_url) 

    x = response.json() 

    if x["cod"] != "404":

        weather = "Temperature : " + str(round(x["main"]["temp"] - 273 , 2))+"°C" +"\nWindSpeed : "+ str(x["wind"]["speed"]) + "\nHumidity : "+ str(x["main"]["humidity"]) +"%"+"\nDescription : "+ str(x["weather"][0]["description"])
        # print (weather)
        return weather
        
    else: 
        return "City not Found ... Check the spelling of the city"