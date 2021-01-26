import requests
import json

with open("username.txt") as f:
    username = f.read()
with open("ipadress.txt") as f:
    ipadress = f.read()

class LightGroup:
    def __init__(self, group_id):
        self.group_id = group_id
        self.on = True
        self.hue = 30000
        self.sat = 254
        self.bri = 254
        self.username = username
        self.ipadress = ipadress

    def update_values(self, on, hue, sat, bri):
        self.on = on
        self.hue = hue
        self.sat = sat
        self.bri = bri

    def update(self):
        messagebody = {
            "on": self.on,
            "hue": self.hue,
            "sat": self.sat,
            "bri": self.bri,
        }
        url = "https://" + self.ipadress + "/api/" + self.username + "/groups/" + str(self.group_id) + "/action"
        x = requests.put(url, data=json.dumps(messagebody), verify=False)
        return x