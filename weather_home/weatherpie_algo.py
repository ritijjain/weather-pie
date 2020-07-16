import os
import requests
from geopy.geocoders import Nominatim
import json
import datetime

class weatherpie_algo_class():
    light_rain = [200, 230, 231, 300, 301, 310, 500]
    rain = [201, 202, 232, 302, 311, 312, 313, 314, 321, 501, 502, 503, 504, 511, 520, 521, 522, 531]
    light_snow = [600, 612, 615, 620]
    snow = [601, 602, 611, 613, 616, 621, 622]

    def __init__(self, user_name, user_location, units):
        self.user_name = user_name
        self.user_location = user_location
        self.units = units

        self.latitude = 0
        self.longitude = 0
        self.location = 0
        self.data = 0

        self.weather_info = {}
        self.weather_out = {}


        self.clothing1 = []
        self.clothing2 = []
        self.clothing3 = []
        self.clothing4 = []
        self.clothing5 = []
    


    def unit_c(self, k):
        return int(k-273.15)

    def unit_f(self, k):
        return int(((k-273.15)*9/5) + 32)

    def dt(self, unix):
        return datetime.datetime.utcfromtimestamp(unix).strftime('%m/%d %H:%M')

    def dthm(self, unix):
        return datetime.datetime.utcfromtimestamp(unix).strftime('%H:%M')

    def latlon(self):
        geolocator = Nominatim(user_agent='WeatherPie')
        self.location = geolocator.geocode(self.user_location)
        self.latitude = self.location.latitude
        self.longitude = self.location.longitude

    def weather_api_call(self):
        self.latlon()
        print('Fetching data for '+ str(self.location.address))
        url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}'.format(self.latitude,self.longitude, os.environ['OPEN_WEATHER_API_KEY'])
        self.data = requests.get(url)
        self.data = self.data.json()

        
        #meta
        self.weather_info['api_call'] = self.data
        self.weather_info['location'] = str(self.location.address)
        self.weather_info['time'] = self.dt(self.data['current']['dt'] + self.data['timezone_offset'])

        #current now
        self.weather_info['temp'] = self.data['current']['temp']
        self.weather_info['feels_like'] = self.data['current']['feels_like']
        self.weather_info['wind'] = self.data['current']['wind_speed']
        self.weather_info['uvi'] = self.data['current']['uvi']
        self.weather_info['condition'] = self.data['current']['weather'][0]['description']

        #current day
        self.weather_info['sunrise'] = self.dthm(self.data['current']['sunrise'] + self.data['timezone_offset'])
        self.weather_info['sunset'] = self.dthm(self.data['current']['sunset'] + self.data['timezone_offset'])
        self.weather_info['high'] = self.data['daily'][0]['temp']['max']
        self.weather_info['low'] = self.data['daily'][0]['temp']['min']
    

        self.weather_info['icon'] = self.data['current']['weather'][0]['icon']
        self.weather_info['now_id'] = self.data['current']['weather'][0]['id']
        
    def clothes_logic(self):

        sun_gear = 'Sun protection – sunglasses, sunscreen, hat'
        summer_clothes = 'Summer clothes – shorts, t-shirt'
        winter_clothes = 'Winter clothes – jacket, pants'
        wind_gear = 'Wind protection – Windcheater, scarf'
        light_rain_gear = 'Light rain protection – umbrella, water resistant shoes'
        rain_gear = 'Rain protection - umbrella, rain jacket, rain boots'
        light_snow_gear = 'Light snow protection – water resistant jacket'
        snow_gear = 'Snow protection – water resistant jacket, gloves, snow boots'
        regular_clothes = 'Regular clothes'

        #Clothing1 i0 - i2
        for i in range(0,2):
            if self.data['current']['uvi'] > 5:
                self.clothing1.append(sun_gear)
            
            if self.data['hourly'][i]['feels_like'] > 304:
                self.clothing1.append(summer_clothes)
            
            if self.data['hourly'][i]['feels_like'] < 280:
                self.clothing1.append(winter_clothes)
            
            if self.data['hourly'][i]['wind_speed'] > 12:
                self.clothing1.append(wind_gear)

            for k in self.data['hourly'][i]['weather']:
                if k['id'] in self.light_rain:
                    self.clothing1.append(light_rain_gear)
                if k['id'] in self.rain:
                    self.clothing1.append(rain_gear)
                if k['id'] in self.light_snow:
                    self.clothing1.append(light_snow_gear)
                if k['id'] in self.snow:
                    self.clothing1.append(snow_gear)
        
        if self.clothing1 == []:
            self.clothing1.append(regular_clothes)
        self.clothing1 = list(dict.fromkeys(self.clothing1))

        
        #Clothing2 i3 - i6
        for i in range(3,6):
            if self.data['hourly'][i]['feels_like'] > 304:
                self.clothing2.append(summer_clothes)
            
            if self.data['hourly'][i]['feels_like'] < 280:
                self.clothing2.append(winter_clothes)
            
            if self.data['hourly'][i]['wind_speed'] > 12:
                self.clothing2.append(wind_gear)

            for k in self.data['hourly'][i]['weather']:
                if k['id'] in self.light_rain:
                    self.clothing2.append(light_rain_gear)
                if k['id'] in self.rain:
                    self.clothing2.append(rain_gear)
                if k['id'] in self.light_snow:
                    self.clothing2.append(light_snow_gear)
                if k['id'] in self.snow:
                    self.clothing2.append(snow_gear)
        
        if self.clothing2 == []:
            self.clothing2.append(regular_clothes)
        self.clothing2 = list(dict.fromkeys(self.clothing2))
        
        #Clothing3 i7 - i12
        for i in range(7,12):
            if self.data['hourly'][i]['feels_like'] > 304:
                self.clothing3.append(summer_clothes)
            
            if self.data['hourly'][i]['feels_like'] < 280:
                self.clothing3.append(winter_clothes)
            
            if self.data['hourly'][i]['wind_speed'] > 12:
                self.clothing3.append(wind_gear)

            for k in self.data['hourly'][i]['weather']:
                if k['id'] in self.light_rain:
                    self.clothing3.append(light_rain_gear)
                if k['id'] in self.rain:
                    self.clothing3.append(rain_gear)
                if k['id'] in self.light_snow:
                    self.clothing3.append(light_snow_gear)
                if k['id'] in self.snow:
                    self.clothing3.append(snow_gear)
        
        if self.clothing3 == []:
            self.clothing3.append(regular_clothes)
        self.clothing3 = list(dict.fromkeys(self.clothing3))

        #Clothing4 i13 - i24
        for i in range(13,24):
            if self.data['hourly'][i]['feels_like'] > 304:
                self.clothing4.append(summer_clothes)
            
            if self.data['hourly'][i]['feels_like'] < 280:
                self.clothing4.append(winter_clothes)
            
            if self.data['hourly'][i]['wind_speed'] > 12:
                self.clothing4.append(wind_gear)

            for k in self.data['hourly'][i]['weather']:
                if k['id'] in self.light_rain:
                    self.clothing4.append(light_rain_gear)
                if k['id'] in self.rain:
                    self.clothing4.append(rain_gear)
                if k['id'] in self.light_snow:
                    self.clothing4.append(light_snow_gear)
                if k['id'] in self.snow:
                    self.clothing4.append(snow_gear)
        
        if self.clothing4 == []:
            self.clothing4.append(regular_clothes)
        self.clothing4 = list(dict.fromkeys(self.clothing4))

        #Clothing5 i25 - i48
        for i in range(25,48):
            if self.data['hourly'][i]['feels_like'] > 304:
                self.clothing5.append(summer_clothes)
            
            if self.data['hourly'][i]['feels_like'] < 280:
                self.clothing5.append(winter_clothes)
            
            if self.data['hourly'][i]['wind_speed'] > 12:
                self.clothing5.append(wind_gear)

            for k in self.data['hourly'][i]['weather']:
                if k['id'] in self.light_rain:
                    self.clothing5.append(light_rain_gear)
                if k['id'] in self.rain:
                    self.clothing5.append(rain_gear)
                if k['id'] in self.light_snow:
                    self.clothing5.append(light_snow_gear)
                if k['id'] in self.snow:
                    self.clothing5.append(snow_gear)
        
        if self.clothing5 == []:
            self.clothing5.append(regular_clothes)
        self.clothing5 = list(dict.fromkeys(self.clothing5))

    def time_list(self):
        current = self.data['hourly'][0]['dt'] + self.data['timezone_offset']
        tl = []
        tl.append(self.dt(current) + ' - ' + self.dt(current + 7200))
        tl.append(self.dt(current + 10800) + ' - ' + self.dt(current + 21600))
        tl.append(self.dt(current + 25200) + ' - ' + self.dt(current + 43200))
        tl.append(self.dt(current + 46800) + ' - ' + self.dt(current + 86400))
        tl.append(self.dt(current + 90000) + ' - ' + self.dt(current + 169200))

        return tl

    def ret(self):
        self.weather_api_call()
        self.clothes_logic()

        return_dic = {}

        return_dic.update(self.weather_info)

        return_dic['time_list'] = self.time_list()

        if self.units == 'metric':
            return_dic['temp'] = self.unit_c(self.weather_info['temp'])
            return_dic['feels_like'] = self.unit_c(self.weather_info['feels_like'])
            return_dic['high'] = self.unit_c(self.weather_info['high'])
            return_dic['low'] = self.unit_c(self.weather_info['low'])
        
        if self.units == 'imperial':
            return_dic['temp'] = self.unit_f(self.weather_info['temp'])
            return_dic['feels_like'] = self.unit_f(self.weather_info['feels_like'])
            return_dic['high'] = self.unit_f(self.weather_info['high'])
            return_dic['low'] = self.unit_f(self.weather_info['low'])
        
        return_dic['clothing_list'] = [self.clothing1, self.clothing2, self.clothing3, self.clothing4, self.clothing5]

        return return_dic