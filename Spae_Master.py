import sklearn
import time
import pandas as pd
import requests
#import eel

#eel.init('web')
print("Spae")

#change bg gradient color according to 3 weathers
#weather condition + max temp

#@eel.expose
def today():
    t = time.localtime()
    day = str(t.tm_mday)
    month = str(t.tm_mon)
    year = str(t.tm_year)
    dash = '-'
    t_info = day + '-' + month + '-' + year
    #eel.printTHIS(t_info)
    return t_info

#@eel.expose
def weather():
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=8da365f65510cd3b548ab105287b6f28&q=Istanbul'
    json_data = requests.get(url).json()
    w_c = json_data['weather'][0]['description']
    w_t = json_data['main']['temp']
    w = w_c + ' - Istanbul'
    #eel.printWeather(w)
    #eel.printTemp(w_t)
    return w

#eel.start('master.html', size=(900, 500))
