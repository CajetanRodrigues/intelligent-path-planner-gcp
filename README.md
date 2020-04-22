# IntelligentPathPlanningUAV Documentation
![drone](https://github.com/CajetanRodrigues/IntelligentPathPlanningUAV/blob/master/ReferenceImages/drone.jpg)
![path](https://github.com/CajetanRodrigues/IntelligentPathPlanningUAV/blob/master/ReferenceImages/path.PNG)
![path](https://github.com/CajetanRodrigues/IntelligentPathPlanningUAV/blob/master/ReferenceImages/drone1.jpg)

*First off, fork the repository, if you wish to contribute*

*Else, if you wish to use this as a base to build something new, go ahead!*

## Steps

>1. Install the modules via pip package
```
pip install requirements.txt
```

>2. Add your Google API key in the 'secret' variable defined.
    As we had security seriously, I have stored the api key securely in the aws secrets manager.
    I retrieve it from there. For your  case, just replace the get_secret() function with your 
    actual key for testing

If you dont have it, go ahead to GCP and create one.
Add the Directions API to the list of services for your created credential
![gcp](https://github.com/CajetanRodrigues/IntelligentPathPlanningUAV/blob/master/ReferenceImages/gcp.PNG)

>3. Use POSTMAN for testing the api

```
http://127.0.0.1:5000/intelligent-path-planning
```
![postman](https://github.com/CajetanRodrigues/IntelligentPathPlanningUAV/blob/master/ReferenceImages/postman.PNG)

## Sample Input

```
{
    "src": {
        "lat": 19.04468,
        "lon": 72.820829
    },
    "des": {
        "lat": 19.055458,
        "lon": 72.827342
    }
}
```
## Sample Output
```
{
    "geocoded_waypoints": [
        {
            "geocoder_status": "OK",
            "place_id": "ChIJi2g3RE_J5zsR4U7yX5Xprp4",
            "types": [
                "street_address"
            ]
        },
        {
            "geocoder_status": "OK",
            "place_id": "ChIJqxCKcUDJ5zsRrSGZvrUzRys",
            "types": [
                "doctor",
                "establishment",
                "health",
                "point_of_interest"
            ]
        }
    ],
    "routes": [
        {
            "bounds": {
                "northeast": {
                    "lat": 19.0554369,
                    "lng": 72.8277906
                },
                "southwest": {
                    "lat": 19.0445833,
                    "lng": 72.8191573
                }
            },
            "copyrights": "Map data ©2020",
            "legs": [
                {
                    "distance": {
                        "text": "1.9 km",
                        "value": 1896
                    },
                    "duration": {
                        "text": "8 mins",
                        "value": 458
                    },
                    "end_address": "1st Floor , Holy Family, next to Hersheys Bakery, Bandra West, Mumbai, Maharashtra 400050, India",
                    "end_location": {
                        "lat": 19.0554369,
                        "lng": 72.8277906
                    },
                    "start_address": "Zafar Baba Hill People Society, 28, Kadeshwari Mandir Marg, Behind, Bandra West, Mumbai, Maharashtra 400050, India",
                    "start_location": {
                        "lat": 19.0445833,
                        "lng": 72.82073969999999
                    },
                    "steps": [
                        {
                            "distance": {
                                "text": "0.2 km",
                                "value": 170
                            },
                            "duration": {
                                "text": "1 min",
                                "value": 59
                            },
                            "end_location": {
                                "lat": 19.0448958,
                                "lng": 72.8191573
                            },
                            "html_instructions": "Head <b>west</b> on <b>Father Angels Ashram Rd</b> toward <b>BJ Road</b><div style=\"font-size:0.9em\">Restricted usage road</div>",
                            "polyline": {
                                "points": "ssfsBsxm{LYzBM`AANCPM`ACX"
                            },
                            "start_location": {
                                "lat": 19.0445833,
                                "lng": 72.82073969999999
                            },
                            "travel_mode": "DRIVING"
                        },
                        {
                            "distance": {
                                "text": "1.3 km",
                                "value": 1292
                            },
                            "duration": {
                                "text": "5 mins",
                                "value": 282
                            },
                            "end_location": {
                                "lat": 19.0541494,
                                "lng": 72.8245261
                            },
                            "html_instructions": "Turn <b>right</b> at Father Agnel Ashram onto <b>BJ Road</b><div style=\"font-size:0.9em\">Pass by Sarkar Heritage (on the right)</div>",
                            "maneuver": "turn-right",
                            "polyline": {
                                "points": "sufsBwnm{LyBo@_AW_AWq@Km@AoAMYEYGiA_@{Bq@w@Yq@Yi@WiEwB{A{@q@MQCg@CUAkAKUEQCgC[mASQEUGUIQGSISISIQISKSKSOOMOOKOKSGUESCYCY?A?E@QBSD[?A?Q@e@HcB"
                            },
                            "start_location": {
                                "lat": 19.0448958,
                                "lng": 72.8191573
                            },
                            "travel_mode": "DRIVING"
                        },
                        {
                            "distance": {
                                "text": "0.4 km",
                                "value": 367
                            },
                            "duration": {
                                "text": "2 mins",
                                "value": 91
                            },
                            "end_location": {
                                "lat": 19.0548343,
                                "lng": 72.8277593
                            },
                            "html_instructions": "Turn <b>left</b> at Apple Certified Associate Service Macbook iPhone iPad iWatch Service Support onto <b>Hill Rd</b><div style=\"font-size:0.9em\">Pass by St Andrews Cemetery (on the left)</div>",
                            "maneuver": "turn-left",
                            "polyline": {
                                "points": "mohsBipn{Lg@SOIGEGKEGEMG[C[A[AKAKIyAA_@QoC?sACuB"
                            },
                            "start_location": {
                                "lat": 19.0541494,
                                "lng": 72.8245261
                            },
                            "travel_mode": "DRIVING"
                        },
                        {
                            "distance": {
                                "text": "67 m",
                                "value": 67
                            },
                            "duration": {
                                "text": "1 min",
                                "value": 26
                            },
                            "end_location": {
                                "lat": 19.0554369,
                                "lng": 72.8277906
                            },
                            "html_instructions": "Turn <b>left</b> at Holi Family Hospital onto <b>Somnath Lane</b><div style=\"font-size:0.9em\">Destination will be on the left</div>",
                            "maneuver": "turn-left",
                            "polyline": {
                                "points": "ushsBodo{LC?uBE"
                            },
                            "start_location": {
                                "lat": 19.0548343,
                                "lng": 72.8277593
                            },
                            "travel_mode": "DRIVING"
                        }
                    ],
                    "traffic_speed_entry": [],
                    "via_waypoint": []
                }
            ],
            "overview_polyline": {
                "points": "ssfsBsxm{Lm@~EQzAyDgA_AWq@Km@AoAMs@MeEqAiBs@sFoC{A{@q@My@GaBMg@IuEo@g@MoAe@mAk@c@][_@Si@Im@As@HcAJiCw@]OQKUKw@Cg@_@uGCiEyBE"
            },
            "summary": "BJ Road",
            "warnings": [],
            "waypoint_order": []
        }
    ],
    "status": "OK"
}
```

## AWS EC2 Linux Instance

![aws](https://github.com/CajetanRodrigues/IntelligentPathPlanningUAV/blob/master/ReferenceImages/aws.PNG)


## AWS Secrets Manager

![aws_secret_key](https://github.com/CajetanRodrigues/IntelligentPathPlanningUAV/blob/master/ReferenceImages/aws_secret_key.PNG)


## Requesting the flask app RESTful API hosted on AWS EC2 instance which is hooked to the AWS Secrets Manager

![postman_aws](https://github.com/CajetanRodrigues/IntelligentPathPlanningUAV/blob/master/ReferenceImages/postman.PNG)

## Import APIs in your POSTMAN application
*Use the link below to import the apis in your postman app*

```
https://explore.postman.com/templates/7542/intelligentpathplanning
```

![postman_template](https://github.com/CajetanRodrigues/IntelligentPathPlanningUAV/blob/master/ReferenceImages/postman_template.PNG)


## View the published Documentation

```
https://documenter.getpostman.com/view/6651486/Szf83UEz?version=latest#d9b039e0-c325-497c-bed0-2528ce966507
```

![postman_intelligent_path_planning](https://github.com/CajetanRodrigues/IntelligentPathPlanningUAV/blob/master/ReferenceImages/postman_intelligent_path_planning.PNG)

![postman_generate_waypoints](https://github.com/CajetanRodrigues/IntelligentPathPlanningUAV/blob/master/ReferenceImages/postman_generate_waypoints.PNG)

