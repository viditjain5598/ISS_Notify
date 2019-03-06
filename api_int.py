import requests
import json
parameters = {"lat" : 28.61 , "lon" : 70.2}

reponse = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

print(reponse.content)