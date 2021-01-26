"""
Changes lights based on outside weather
"""

import json
import time
import sys
import datetime
from yr.libyr import Yr
from light_group import LightGroup
#print("sunrise", sunrise)
#print("sunset", sunset)

#print(now)
#print(now["symbol"]["@name"])

cmd_args = sys.argv
if len(cmd_args) > 1:
    light_group = LightGroup(cmd_args[1])
else:
    light_group = LightGroup(3)
light_group.transition_time = 600

COLD_LIGHT = [40000, 50, 100]
WARM_LIGHT = [10000, 150, 254]
NEUTRAL_LIGHT = [10000, 150, 150]
SUNDOWN_LIGHT = [10000, 150, 120]

# You can see what each symbol looks like here:
# https://hjelp.yr.no/hc/en-us/articles/203786121-Weather-symbols-on-Yr
cold_light_weather = ['fair', 'clearsky']

warm_light_weather = [ 'lightsnowandthunder','lightsnow',
                       "lightsleetandthunder", 'lightrainandthunder',
                       'heavysleet', 'lightsleet',
                       'rainandthunder', 'heavysnowandthunder', 'rain', 'snow',
                        'cloudy',  'heavyrain', 'lightrain',
                       'heavysleetandthunder',   'fog', 'sleet',  'heavysnow',
                       'snowandthunder', 'sleetandthunder',
                       'heavyrainandthunder']

neutral_light_weather = ['partlycloudy','rainshowers',
                         'lightssnowshowersandthunder','heavyrainshowers',
                         'lightssleetshowersandthunder','heavysleetshowers',
                         'snowshowersandthunder','heavysnowshowers',
                         'sleetshowersandthunder','lightrainshowersandthunder',
                         'lightrainshowers','heavyrainshowersandthunder',
                         'heavysnowshowersandthunder','rainshowersandthunder',
                         'heavysleetshowersandthunder','sleetshowers',
                         'lightsleetshowers','lightsnowshowers','snowshowers']


while True:
    weather = Yr(location_name="Norway/Trøndelag/Trondheim/Trondheim")
    weather_now = weather.now(as_json=True)
    weather_now = json.loads(weather_now)
    print(weather_now)
    sunrise_sunset = weather.dictionary["weatherdata"]["sun"]
    sunrise = sunrise_sunset["@rise"]
    sunset = sunrise_sunset["@set"]
    sunrise = datetime.datetime.strptime(sunrise, "%Y-%m-%dT%H:%M:%S")
    sunset = datetime.datetime.strptime(sunset, "%Y-%m-%dT%H:%M:%S")

    time_now = datetime.datetime.now()

    weather_nom_symbol = weather_now["symbol"]["@name"]
    if not sunrise < time_now < sunset:
        light_group.update_values(True, *SUNDOWN_LIGHT)
    elif weather_nom_symbol in warm_light_weather:
        light_group.update_values(True, *WARM_LIGHT)
    elif weather_nom_symbol in cold_light_weather:
        light_group.update_values(True, *COLD_LIGHT)
    elif weather_nom_symbol in neutral_light_weather:
        light_group.update_values(True, *COLD_LIGHT)
    else:
        print("Unknown weather symbol: ", weather_nom_symbol)

    print(light_group.update().text)

    time.sleep(600)