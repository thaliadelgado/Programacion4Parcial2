# Libraries
import requests as requests

import json
import os
import csv
from flask import Flask, request
from flask import jsonify

# Dictionaries
data = {}
head = {}

# Process of charge of variables
with open('./csv/data.csv', encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:

        if 'Country Name' in row['\ufeff"Data Source"']:
            data[0] = row

        if 'Panamá' in row['\ufeff"Data Source"']:
            data[1] = row

with open('./json/data.json', 'w') as file:
    json.dump(data, file, indent=4)


app = Flask(__name__)
app.secret_key = os.urandom(128)

@app.route("/api/worldbank/data", methods=["POST", "GET"])
def data():
    with open('./json/data.json') as file:
        data = json.load(file)
        return data

@app.route('/api/worldbank/data/years', methods=["POST", "GET"])
def data_years():
    with open('./json/data.json') as file:
        resp = json.load(file)
        data = resp['0']
        return '{}'.format(data['null'])

@app.route('/api/worldbank/data/panama', methods=["POST", "GET"])
def data_panama():
    with open('./json/data.json') as file:
        resp = json.load(file)
        data = resp['1']
        return '{}'.format(data)

@app.route('/api/worldbank/data/panama_in_years', methods=["POST", "GET"])
def data_panama_in_years():
    with open('./json/data.json') as file:
        resp = json.load(file)
        data = resp['1']
        data2 = resp['0']
        return '{}\n{}'.format(data2['null'],data)

if __name__ == '__main__':
    app.run(debug=True)