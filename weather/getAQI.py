# -*- coding: utf-8 -*-
import urllib3
import urllib2
import json
import requests


class cityAQI(object):
    """
    params:
        aqi: int
        sources: [string]
        dominentPol:str
        aqiDetail:dict
        MeasureLocalTime:str
    """
    APIkey = '6f5c10159caf14c96c762ddb6690b23d1d7b7aef'
    urlHead = 'http://api.waqi.info/feed/'
    urlTail = '/?token='+APIkey
    
    def __init__(self, city=''):
        if city == '':
            print('city name (string) missing')
            return
        self.cityName = city
    
    def paramsUpdate(self,aqiData):
        self.aqi = aqiData['aqi']
        self.sources = []
        for s in aqiData['attributions']:
            self.sources.append(s['name'])
        self.dominentPol = aqiData['dominentpol']
        self.aqiDetail = aqiData['iaqi']
        self.MeasureLocalTime = aqiData['time']['s']

    
    def update(self):
        url = self.urlHead+self.cityName+self.urlTail
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
            aqiByte = response.read()
            aqiData = str(aqiByte)
            aqiDict = json.loads(aqiData)
            self.paramsUpdate(aqiDict['data'])



test = cityAQI('beijing')
test.update()
