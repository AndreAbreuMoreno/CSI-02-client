from flask import Flask
from flask import render_template
import json
import requests

app = Flask(__name__)


@app.route('/cidade/<nome_da_cidade>')
def cidade(nome_da_cidade):

    req = requests.get('http://pibdascidades.herokuapp.com/pib', params={'cidade': nome_da_cidade})
    print(req.content.decode())
    city = json.loads(req.content.decode())['data']

    return render_template('cidades.html', city=city)


@app.route('/')
def index():
    return render_template('index.html', hello='Hello World')


if __name__ == '__main__':
    app.run()
