from flask import Flask
from flask import render_template
import json
import requests

from flask import request, redirect, url_for

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


@app.route('/nome_cidade', methods=['GET', 'POST'])
def nome_cidade():
    if request.method == 'POST':
        nome_da_cidade = request.form.get('nome_da_cidade')
        return redirect(url_for('cidade', nome_da_cidade=nome_da_cidade))
    return render_template('nome_cidade.html')


if __name__ == '__main__':
    app.run()

