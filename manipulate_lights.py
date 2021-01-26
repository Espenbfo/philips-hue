"""
Rainbow pattern lights
"""

import json
import sys
import time
import requests

# Username and ip adress in seperate files
with open("username.txt") as f:
    username = f.read()
with open("ipadress.txt") as f:
    ipadress = f.read()

type = "groups"  # lights or groups

# The id of your chosen light or group
id = 3

if type == "groups":
    url = "https://" + ipadress + "/api/" + username + "/groups/" + str(id) + "/action"
elif type == "lights":
    url = "https://" + ipadress + "/api/" + username + "/lights/" + str(id) + "/state"

messagebody = {
    "on": True,
    "hue": 30000,
    "sat": 254,
    "bri": 254,
    "transitiontime": 7
}

print(json.dumps(messagebody))

last_time = time.time()
while True:
    current_time=time.time()
    last_time,messagebody["transitiontime"] = current_time,int((current_time- last_time)*100)+1
    print(messagebody["transitiontime"])
    messagebody["hue"] = (messagebody["hue"]+1000)%65000
    response = requests.put(url, data = json.dumps(messagebody), verify=False)

    while (response.status_code != 200):
        print("hei")
        time.sleep(1.0)
    print(response.text)