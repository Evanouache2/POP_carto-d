import requests
import smtplib
import urllib
import geopy
import json
import numpy 
import matplotlib.pyplot as plt
import smopy 


import Config





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
        
        
        
def get_info_area () :
    var = (input("\nNuméro de zone : "))
    print ""
    print "Coordonnees : ", geocode[var]
    print ""
    print'Météo à ces coordonnées : \n\n', weathercode[var]
    
    
        
def get_area(lat_min, lat_max, lon_min, lon_max) :
    
    lat_min = lat_max = float (geocode[0]['lat'])
    lon_min = lon_max = float (geocode[0]['lon'])
    
    a = 0
    
    for loc in geocode : 
        lat_min = min(lat_min, float(geocode[a]['lat']))
        lat_max = max(lat_max, float(geocode[a]['lat']))
        lon_min = min(lon_min, float(geocode[a]['lon']))
        lon_max = max(lon_max, float(geocode[a]['lon']))
        
        a += 1
        
    marge_lon = ((lon_max - lon_min)/100)*10
    marge_lat = ((lat_max - lat_min)/100)*10
    
    lat_min -= marge_lat
    lat_max += marge_lat
    lon_min -= marge_lon
    lon_max += marge_lon
        
    return (lat_min, lat_max, lon_min, lon_max)
  
  
  
  
  
    
def get_map (lat_min, lat_max, lon_min, lon_max) :
    
    map = smopy.Map(lat_min, lon_min,lat_max,lon_max, z=3)
    
    a = 0
    ax = map.show_mpl(figsize=(8,6))
    
    for loc in geocode :
        x,y = map.to_pixels(float(geocode[a]['lat']), float(geocode[a]['lon']))
        ax.plot(x,y, 'or', ms=5, mew=1)
        
        a += 1
        
    plt.show()
    return True

    
    
    
    
geocode=[]
weathercode=[]

lat_min = 0 
lat_max = 0
lon_min = 0 
lon_max = 0

get_location()
get_weather()

get_area(lat_min, lat_max, lon_min, lon_max)
get_map (lat_min, lat_max, lon_min, lon_max)

