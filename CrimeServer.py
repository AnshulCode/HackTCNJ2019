from flask import Flask
import requests
import recieveJSON
import json

CrimeServer = Flask(__name__)

@CrimeServer.route('/')
def apiRequest():
    s = ""
    y = recieveJSON.getRestaurants("restaurants", -74.7771916 , 40.272249099999996, 50)['businesses']
    for i in y:
        s+= i['name'] + "<br/>"
    return s
if __name__ == '__main__':
    CrimeServer.run() 