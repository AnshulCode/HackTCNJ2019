from flask import Flask
import requests
import recieveJSON
import json

Rinder = Flask(__name__)

@Rinder.route('/')
def apiRequest():
    s = ""
    y = recieveJSON.getRestaurants("restaurants", -74.7771916 , 40.272249099999996, 50)['businesses']
    for i in y:
        s+= i['name'] + "<br/>"
    return s
if __name__ == '__main__':
    Rinder.run(host='0.0.0.0') 