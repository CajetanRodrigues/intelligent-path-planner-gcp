# Import all modules
import requests 
import flask
import json
from flask import request

app = flask.Flask(__name__)  

@app.route('/intelligent-path-planning', methods=['POST'])
def home(): 
    
    # Fetching Input data from the POST request
    data = request.json
    srcLat = data['src']['lat']
    srcLon = data['src']['lon']
    desLat = data['des']['lat']
    desLon = data['des']['lon']
    
    # Configuring the google maps directions API
    URL = "https://maps.googleapis.com/maps/api/directions/json?origin="+str(srcLat)+","+str(srcLon)+"&destination="+str(desLat)+","+str(desLon)+"&key=" + "PASTE_YOUR_API_KEY_HERE"
  
    # Initiating a get request using the inbuilt python requests library
    r = requests.get(url = URL) 
    data = r.json() 
    return json.dumps(data)

if __name__ == "__main__":
    app.run()