import os
import numpy as np
import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='web', static_folder='static')

x = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]

def predict(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10):
    y = []
    y.append(v1)
    y.append(v2)
    y.append(v3)
    y.append(v4)
    y.append(v5)
    y.append(v6)
    y.append(v7)
    y.append(v8)
    y.append(v9)
    y.append(v10)
    f = np.polyfit(x, y, 2)
    m = np.poly1d(f)
    p = round(m(1), 2)
    return p

@app.route('/', methods=["GET", "POST"])
def index():
    city = str(request.values.get('test'))

    url1 = "http://api.openweathermap.org/data/2.5/forecast?q="
    url2 = "&appid=8da365f65510cd3b548ab105287b6f28"
    url = url1 + city + url2

    json_data = requests.get(url).json()
    temp = round(((json_data['list'][0]['main']['temp']) - 273), 1)
    t1 = round(((json_data['list'][1]['main']['temp']) - 273), 1)
    t2 = round(((json_data['list'][4]['main']['temp']) - 273), 1)
    t3 = round(((json_data['list'][7]['main']['temp']) - 273), 1)
    t4 = round(((json_data['list'][10]['main']['temp']) - 273), 1)
    t5 = round(((json_data['list'][13]['main']['temp']) - 273), 1)
    t6 = round(((json_data['list'][16]['main']['temp']) - 273), 1)
    t7 = round(((json_data['list'][19]['main']['temp']) - 273), 1)
    t8 = round(((json_data['list'][22]['main']['temp']) - 273), 1)
    t9 = round(((json_data['list'][25]['main']['temp']) - 273), 1)
    t10 = round(((json_data['list'][28]['main']['temp']) - 273), 1)

    p = predict(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10)
    w = json_data['list'][0]['weather'][0]['description']
    weather = w.capitalize() 

    return render_template('index.html', t=temp, w=weather, n=p)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
