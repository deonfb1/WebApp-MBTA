''' Need to update the flask portion to make it work'''

import urllib.request
import json
from pprint import pprint
from flask import Flask

MAPQUEST_API_KEY = 'bIghmxjhSowXsNMQ2VpO4AGApPJ8uspv'
def MBTA(place_name):
    name = place_name.replace(" ", "")
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={name}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    lat = response_data['results'][0]['locations'][0]['latLng']['lat']
    lng = response_data['results'][0]['locations'][0]['latLng']['lng']

    MAPAPI = 'bed52263c12541bcb2037c549df9fc17'
    url2 = f'https://api-v3.mbta.com/stops?api_key={MAPAPI}&sort&filter[latitude]={lat}&filter[longitude]={lng}&filter[radius]=1'
    f2 = urllib.request.urlopen(url2)
    response_text2 = f2.read().decode('utf-8')
    response_data2 = json.loads(response_text2)
    pprint(response_data2['data'][0]['attributes'])

app = Flask(__name__)

@app.route('/')
@app.route('/mbta')
def nearest(place_name):
    place_name = input("Where to?")
    name = place_name.replace(" ", "")
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={name}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    lat = response_data['results'][0]['locations'][0]['latLng']['lat']
    lng = response_data['results'][0]['locations'][0]['latLng']['lng']

    MAPAPI = 'bed52263c12541bcb2037c549df9fc17'
    url2 = f'https://api-v3.mbta.com/stops?api_key={MAPAPI}&sort&filter[latitude]={lat}&filter[longitude]={lng}&filter[radius]=1'
    f2 = urllib.request.urlopen(url2)
    response_text2 = f2.read().decode('utf-8')
    response_data2 = json.loads(response_text2)
    return "Howdy folks"
    #response_data2['data'][0]['attributes']

