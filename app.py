# Import all modules
import requests 
import flask
import json
from flask import request
import boto3
import base64
from botocore.exceptions import ClientError

# Flask app for RESTful APIs
app = flask.Flask(__name__)  

# Given src and dest coordinates, fetch route information
@app.route('/intelligent-path-planning', methods=['POST'])
def intelligentPathPlanning(): 
    
    # Fetching Input data from the POST request
    data = request.json
    srcLat = data['src']['lat']
    srcLon = data['src']['lon']
    desLat = data['des']['lat']
    desLon = data['des']['lon']
    
    # Fetching the secret key stored in AWS Secrets Manager. You can replace your key here, but it has security flaws
    secret = get_secret()   
    secret = secret[8:47]
    print(secret) 
    # Configuring the google maps directions API
    URL = "https://maps.googleapis.com/maps/api/directions/json?origin="+str(srcLat)+","+str(srcLon)+"&destination="+str(desLat)+","+str(desLon)+"&key=" + secret
    
    # Initiating a get request using the inbuilt python requests library
    r = requests.get(url = URL) 
    data = r.json()
    return json.dumps(data)

# Fetched encrypted key stored in AWS Secrets Manager.
def get_secret():
    
    secret_name = "GoogleMapsAPIkey"
    region_name = "ap-south-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    secret = ''

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId='GoogleMapsAPIkey'
        )
        print(get_secret_value_response)
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return secret
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
    return secret

# Given src and dest, fetch an array of waypoints along with distance left to destination
@app.route('/generate-waypoints', methods=['POST'])
def generateWaypoints(): 
    
    # Fetching Input data from the POST request
    data = request.json
    srcLat = data['src']['lat']
    srcLon = data['src']['lon']
    desLat = data['des']['lat']
    desLon = data['des']['lon']
    
    # Fetching the secret key stored in AWS Secrets Manager. You can replace your key here, but it has security flaws
    secret = get_secret()   
    secret = secret[8:47]
    print(secret) 
    # Configuring the google maps directions API
    URL = "https://maps.googleapis.com/maps/api/directions/json?origin="+str(srcLat)+","+str(srcLon)+"&destination="+str(desLat)+","+str(desLon)+"&key=" + secret
    
    # Initiating a get request using the inbuilt python requests library
    r = requests.get(url = URL) 
    data = r.json()
    routes = data['routes']
    legs = routes[0]['legs']
    steps = legs[0]['steps']
    waypoint_list = []
    for waypoint in steps:
        waypoint_obj = {
            'distanceLeft': waypoint['distance']['value'],
            'waypoint': waypoint['start_location']
        }
        waypoint_list.append(waypoint_obj)
    print(waypoint_list)
    return json.dumps(waypoint_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True,threaded=True)