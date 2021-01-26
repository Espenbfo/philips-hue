import requests
import json
import sys

# Username and ip adress in seperate files
with open("username.txt") as f:
    username = f.read()
with open("ipadress.txt") as f:
    ipadress = f.read()

# The id of your chosen light
light = 5

url = "https://" + ipadress + "/api/" + username + "/lights/" + str(light) + "/state"

cmd_args = sys.argv

messagebody = {
    "on": True,
    "hue": 30000,
    "sat": 254,
    "bri": 254,

}
keys = ["hue", "sat", "bri"]
for i in range(len(cmd_args)-1):
    try:
        messagebody[keys[i]] = int(cmd_args[i+1])
    except:
        print("Error in argument", i, ". Expected int")

x = requests.put(url, data=json.dumps(messagebody), verify=False)

print(x.status_code)
print(x.text)