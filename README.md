# philips-hue
This project is a collection of python files meant to change my hue lights in interesting ways.

## Setup
In order to run any of the python files you need to create two more txt files. If you need help finding the ip address of your bridge or creating a 
user, you can find help here: https://developers.meethue.com/develop/get-started-2/ 
##### ipadress.txt
Is the ipadress of your philips bridge
##### username.txt
Is your philips bridge username

## Documentation
##### change_color.py
This is a simple file that changes the color of one light. It is called from the command line:
```shell 
python change_color.py hue sat bri
```
#### manipulate_lights.py
This file makes a group of lights or a single light change color in a rainbow pattern.

#### yr_api.py
This program changes your lights based on the weather outside, and if the sun is up.
```shell 
python yr_api.py
```