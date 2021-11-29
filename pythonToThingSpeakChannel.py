import requests
import time
import random

baseurl = 'https://api.thingspeak.com/update?api_key=J58C1OSQZNR9KMR9'

while (True):
    randomFloat = random.random()
    temp = 14.00 + randomFloat
    url = baseurl + '&field1=' + str(temp) 
    x = requests.get(url)
    print(x)
    time.sleep( 1 )
    
