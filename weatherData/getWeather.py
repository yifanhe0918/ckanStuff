# -*- coding: utf-8 -*-
import urllib3
import json
import time
import urllib2

class cityInfo(object):
    """
    object contains the weather infos in a city
    params:
        country:str
        city:str
        searchMode:str
        cityID:str
        urlCommon:str
        urlTail:str
        coordinate:('lat','lon')
        
        city:str
        country:str
        weather:str
        weather_description:str
        temperature:float
        temp_max:float
        temp_min:float
        humidity:float (%)
        pressure:float (hPa)
        wind_speed:float (mps)
        wind_deg:float (dgree , from North clock direction)
        sunrise:float
        sunset:float
        
    """
    APIkey = '9542a187a90a6baa689a4db5eebfa432'
    
    def paramsUpdate(self,w_d):
        if self.searchMode != 'cityName':
            self.city = w_d['name']
        if self.searchMode != 'coordinate':
            self.coordinate = (w_d['coord']['lat'], w_d['coord']['lon'])
        if self.searchMode != 'id':
            self.cityID = w_d['id']
        self.country = w_d['sys']['country']
        self.weather = w_d['weather'][0]['main']
        self.weather_description = w_d['weather'][0]['description']
        self.temperature = w_d['main']['temp']-273.15
        self.temp_max = w_d['main']['temp_max']-273.15
        self.temp_min = w_d['main']['temp_min']-273.15
        self.humidity = w_d['main']['humidity']
        self.wind_speed = w_d['wind']['speed']
        if 'deg' in w_d['wind'].keys():
            self.wind_deg = w_d['wind']['deg']
        else:
            self.wind_deg = 'NoData'
        self.pressure = w_d['main']['pressure']
        timeZone = w_d['coord']['lon']//15 + 1
        sunriseUTC = w_d['sys']['sunrise'] + timeZone*3600
        Rise = time.gmtime(sunriseUTC)
        self.sunrise = 'Local-Time  '+str(Rise.tm_hour)+':'+str(Rise.tm_min)+':'+\
        str(Rise.tm_sec)
        sunsetUTC =  w_d['sys']['sunset'] + timeZone*3600
        Set = time.gmtime(sunsetUTC)
        self.sunset = 'Local-Time  '+str(Set.tm_hour)+':'+str(Set.tm_min)+':'+\
        str(Set.tm_sec)
    
    def __init__(self, countryName='', cityName='', searchBy = 'cityName', \
                 coordLatLon = ['0','0'],cityId=''):
        """
        updateTime: update period (second) for the weather infos
        searchMode: search method for the weather infos, including--
                    'cityName','coordinate','id'
        """
        
        self.country = countryName
        self.city = cityName
        self.coordinate = coordLatLon
        self.searchMode = searchBy
        self.cityID = cityId
        
        self.urlCommon = 'http://api.openweathermap.org/data/2.5/weather?'
        self.urlTail = ''
        
        if self.searchMode == 'cityName':
            self.urlTail = 'q=' + cityName +',' + countryName
        elif self.searchMode == 'coordinate':
            self.urlTail = 'lat='+self.coordinate[0]+'&lon='+self.coordinate[1]
        elif self.searchMode == 'id':
            self.urlTail = 'id='+self.cityID            
      
        
    def update(self):
        # http = urllib3.PoolManager()
        url = self.urlCommon + self.urlTail+'&APPID='+self.APIkey
        # r = http.request('GET',url)
        orangeProxy = {'http': '10.193.250.16:8080'}
        proxy = urllib2.ProxyHandler(orangeProxy)
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        code = response.getcode()
        if code != 200:
            print('data require failed ...')
        else:
            weatherDataByte = response.read()
            weatherData = str(weatherDataByte)
            weatherDict = json.loads(weatherData)
            self.paramsUpdate(weatherDict)                


# test = cityInfo(countryName="uk",cityName="london")
# test.update()