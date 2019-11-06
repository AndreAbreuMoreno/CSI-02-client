import os
import requests
from flask import Flask
from flask import render_template
import json
import requests

from flask import request, redirect, url_for

app = Flask(__name__)


def get_lat_lng(city, provincy):
    url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        "q": f"{city},{provincy}",
        "key": os.getenv("OPEN_CAGE_TOKEN")
    }

    answer = requests.get(url, params=params).json()
    lat_lng = answer.get("results")[0].get("geometry")
    return lat_lng


@app.route('/cidade/<nome_da_cidade>')
def cidade(nome_da_cidade):
    req = requests.get('http://pibdascidades.herokuapp.com/pib', params={'cidade': nome_da_cidade})
    city = json.loads(req.content.decode())['data']

    lat_lng = get_lat_lng(city["name"], city["provincy"])

    return render_template('cidades.html',
                           city=city,
                           lat=lat_lng["lat"],
                           lng=lat_lng["lng"])


# @app.route('/')
# def index():
#     # return render_template('index.html', hello='Hello World')
#     return redirect(url_for('nome_cidade'))


@app.route('/', methods=['GET', 'POST'])
def nome_cidade():
    if request.method == 'POST':
        nome_da_cidade = request.form.get('nome_da_cidade')
        return redirect(url_for('cidade', nome_da_cidade=nome_da_cidade))
    return render_template('nome_cidade.html')


@app.route('/')
def index():

    return render_template('index.html')


if __name__ == '__main__':
    app.run()

