from yr.libyr import Yr
import json
import datetime
from light_group import LightGroup
import time

#print("sunrise", sunrise)
#print("sunset", sunset)

#print(now)
#print(now["symbol"]["@name"])

light_group = LightGroup(3)

cold = [40000, 50, 254]
warm = [10000, 150, 254]
while True:
    weather = Yr(location_name="Norway/Trøndelag/Trondheim/Trondheim")
    weather_now = weather.now(as_json=True)
    weather_now = json.loads(weather_now)
    sunrise_sunset = weather.dictionary["weatherdata"]["sun"]
    sunrise = sunrise_sunset["@rise"]
    sunset = sunrise_sunset["@set"]
    sunrise = datetime.datetime.strptime(sunrise, "%Y-%m-%dT%H:%M:%S")
    sunset = datetime.datetime.strptime(sunset, "%Y-%m-%dT%H:%M:%S")

    if weather_now["symbol"]["@name"] == "Cloudy" or weather_now["symbol"]["@name"] == "snow":
        light_group.update_values(True, *warm)
    else:
        light_group.update_values(True, *cold)
    time_now = datetime.datetime.now()
    if sunrise < time_now < sunset:
        light_group.bri = 100
    else:
        light_group.bri = 254
    print(light_group.update().text)

    time.sleep(600)