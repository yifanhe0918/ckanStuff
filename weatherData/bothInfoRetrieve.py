import getAQI
import getWeather

def getPayload(w, a):
    payload = ''
    payload = payload+'wt|'+w.weather+',wtd|'+w.weather_description+',ci|'+w.city
    payload = payload+',co|'+w.country+',tem|'+str(w.temperature)+',hum|'+str(w.humidity)
    payload = payload+',pre|'+str(w.pressure)+',wsp|'+str(w.wind_speed)+',wdg|'
    payload = payload+str(w.wind_deg)+',srs|'+w.sunrise+',sst|'+w.sunset+',aqi|'
    sourceEng = a.sources[0]
    payload = payload+str(a.aqi)+',src|'+sourceEng
    payload = payload+',dmp|'+a.dominentPol+',p25|'+str(a.aqiDetail['pm25']['v'])
    payload = payload+',p10|'+str(a.aqiDetail['pm10']['v'])+',so2|'+str(a.aqiDetail['so2']['v'])
    payload = payload+',o3|'+str(a.aqiDetail['o3']['v'])+',no2|'+ str(a.aqiDetail['no2']['v'])
    payload = payload+',lat|'+str(w.coordinate[0])+',lon|'+str(w.coordinate[1])
    return payload


def retrieveInfo(country,city):
    country_name = country
    city_name = city
    cityWeather = getWeather.cityInfo(countryName=country_name, cityName=city_name)
    cityAQI = getAQI.cityAQI(city=city_name)
    cityWeather.update()
    cityAQI.update()
    message = getPayload(cityWeather, cityAQI)
    return message