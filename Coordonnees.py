import requests
import smtplib
import urllib
import geopy
import json
import Config



geocode=[]
weathercode=[]

def get_location():
    lonlat=open('/home/popschool/projects/Coordonnée/lonlatonly.txt', 'r')
    

    for line in lonlat:
        (lon, lat)=line.split(',')
        coord = {'lat':lat.strip(), 'lon':lon}
        geocode.append(coord)
    
    return geocode
    
      
def get_weather():
    api = Config.apikey
    
    a = 0
        
    for list in geocode:
        
        x = geocode[a]['lon']
        y = geocode[a]['lat']
    
        url='http://api.openweathermap.org/data/2.5/weather?lat='+x+'&lon='+y+'&units=metrics&appid='+api
        weather_r=requests.get(url)
        weather_j=weather_r.json()
        
        name = weather_j["name"]
        visibility = weather_j["visibility"]
        country = weather_j["sys"]["country"]
        timezone = weather_j["timezone"]
        temp = weather_j["main"]["temp"]
        temp_max = weather_j["main"]["temp_max"]
        temp_min = weather_j["main"]["temp_min"]
        humidity = weather_j["main"]["humidity"]
        pressure  =weather_j["main"]["pressure"]
        feels_like = weather_j["main"]["feels_like"]
        wind = weather_j["wind"]
        
        meteo = {'name':name, 'visibility':visibility, 'country':country, 'timezone':timezone, 'temp':temp, 'temp_max':temp_max, 'temp_min':temp_min, 'humidity':humidity, 'pressure':pressure, 'feels_like':feels_like, 'wind':wind}
        
        weathercode.append(meteo)
        
        a += 1
        
        

get_location()
get_weather()

var = (input("\nNuméro de zone : "))
print ""
print "Coordonnees : ", geocode[var]
print ""
print'Météo à ces coordonnées : \n\n', weathercode[var]