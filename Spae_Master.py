import numpy as np
import time
import pandas as pd
import requests
import matplotlib.pyplot as plt
import eel

eel.init('web')
print("Spae")

df = pd.read_csv('final_data.csv')
x_data, y_data = (df["DateTime"].values, df["Avg_Temp"].values)

@eel.expose
def today():
    t = time.localtime()
    day = str(t.tm_mday)
    month = str(t.tm_mon)
    year = str(t.tm_year)
    dash = '-'
    t_info = day + '-' + month + '-' + year
    eel.printTHIS(t_info)
    return t_info

@eel.expose
def weather():
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=8da365f65510cd3b548ab105287b6f28&q=Istanbul'
    json_data = requests.get(url).json()
    w_c = json_data['weather'][0]['description']
    w_p = round(((json_data['main']['temp']) - 273), 1)
    w_t = str(w_p) + "C"
    w = w_c + ' - Istanbul'
    eel.printWeather(w)
    eel.printTemp(w_t)
    return w

def Graph(model, independent_variable, dependent_variable, Name):
    x_new = np.linspace(20, 365, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variable, '.', x_new, y_new, '-')
    plt.title('Istanbul Temp Prediction')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    
    plt.xlabel(Name)
    plt.ylabel('Temperature')

    plt.show()
    plt.close()

@eel.expose
def Prediction():
    f = np.polyfit(x_data, y_data, 2)
    p = np.poly1d(f)
    nom = int(time.strftime('%j'))
    lom = round((p(nom)), 1)
    tom = str(lom) + "C"
    eel.printPrediction(tom)

eel.start('master.html', size=(900, 500))
