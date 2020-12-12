import requests
import json
import sys

#Username and ip adress in seperate files
with open("username.txt") as f:
    username = f.read()
with open("ipadress.txt") as f:
    ipadress = f.read()

#The id of your chosen light
light = 5


url = "https://" + ipadress + "/api/" + username + "/lights/" + str(light) + "/state"

messagebody = {
    "on": True,
    "hue": 30000,
    "sat": 254,
    "bri": 254,
}

print(json.dumps(messagebody))


while True:
    messagebody["hue"] = (messagebody["hue"]+1000)%65000
    
    x = requests.put(url, data = json.dumps(messagebody), verify=False)

    print(x.text)