import requests
import time
import random

baseurl = 'https://sensor-data-example.glitch.me/addData'

while (True):
    randomFloat = random.random()
    tempValue = 14.00 + randomFloat
    myobj = {'field': "temp", 'value': tempValue}
    x = requests.post(baseurl, data = myobj)
    print(x.text)
    time.sleep( 1 )
