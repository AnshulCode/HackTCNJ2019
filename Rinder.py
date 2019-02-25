from flask import Flask
import requests
import recieveJSON
import json
from flask import request
import jsonify
from collections import defaultdict



Rinder = Flask(__name__)

appList = defaultdict(list)

@Rinder.route('/', methods = ['GET','POST'])
def apiRequest():
    
    lon = ""
    lat = ""
    resp = ""
    apiData = ""
    data = ""
   
    if request.method == 'POST':
       resp = request.json
       lon = resp['Lon:']
       lat = resp['Lat:']
       apiData = recieveJSON.getRestaurants("Restaurant", lon, lat , 10)
       print(apiData)
       for i in range(0,len(apiData)):
          data +=  "name:" + apiData[i]['name']+ "," + "address:" + apiData[i]['location']['display_address'][0]+ "" + apiData[i]['location']['display_address'][1]+ "," + "distance:" + str(apiData[i]['distance']/1609) + " "
       print(data)
    
if __name__ == '__main__':
    Rinder.run()   