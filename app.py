from flask import Flask
from flask import render_template
import json
import requests

from flask import request, redirect, url_for

app = Flask(__name__)


@app.route('/cidade/<nome_da_cidade>')
def cidade(nome_da_cidade):

    req = requests.get('http://pibdascidades.herokuapp.com/pib?cidade={}'.format(nome_da_cidade))
    city = json.loads(req.content.decode())

    return render_template('cidades.html', city=city)


@app.route('/')
def index():
    return render_template('index.html', hello='Hello World')


@app.route('/city-info/<language>')
def city_info(language):
    return render_template('city_info.html', language=language)


@app.route('/city-name', methods=['GET', 'POST'])
def city_name():
    if request.method == 'POST':
        language = request.form.get('language')
        return redirect(url_for('city_info', language=language))
    return render_template('city_name.html')


if __name__ == '__main__':
    app.run()


"""
EXAMPLE
@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''
"""