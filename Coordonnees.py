import requests
import smtplib
import urllib
import geopy
import json
import numpy 
import matplotlib.pyplot as plt
import smopy 


import Config





def get_location(geocode):
    lonlat=open('/home/popschool/projects/Coordonnée/lonlatonly.txt', 'r')
    

    for line in lonlat:
        (lon, lat)=line.split(',')
        coord = {'lat':lat.strip(), 'lon':lon}
        geocode.append(coord)
    
    return geocode
    
      
def get_weather(geocode, weathercode):
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
        
        
        
def get_info_area (geocode, weathercode) :
    var = (input("\nNuméro de zone : "))
    print ""
    print "Coordonnees : ", geocode[var]
    print ""
    print'Météo à ces coordonnées : \n\n', weathercode[var]
    
    
        
def get_area(geocode, coord) :
    
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
    
    MinMax= {'lat_min':lat_min,'lat_max':lat_max, 'lon_min':lon_min,'lon_max':lon_max}
    
    coord.append (MinMax)
    return (coord)
  
  
    
def get_map (coord, geocode) :
    
    map = smopy.Map(coord[0]['lon_min'], coord[0]['lat_min'], coord[0]['lon_max'], coord[0]['lat_max'], z=15)
    
    print coord
    
    a = 0
    ax = map.show_mpl(figsize=(8,6))
    
    for loc in geocode :
        x,y = map.to_pixels(float(geocode[a]['lon']), float(geocode[a]['lat']))
        ax.plot(x,y, 'or', ms=10, mew=1)
        
        a += 1
        
    plt.show()

    return True

    
    
def main():
    
    geocode=[]
    weathercode=[]
    
    coord = []
    
    get_location(geocode)
    get_weather(geocode, weathercode)
    
    print '\nAffichage des données météos --> 1'
    print 'Affichage de la map --> 2'
    var = (input("\nEntrez votre choix : "))
    
    if (var == 1):
        get_info_area(geocode, weathercode)
        
    if (var == 2):
        get_area(geocode, coord)
        get_map(coord, geocode)

    if (var != 1):
        if (var !=2):
            print 'Choix invalide'

main()