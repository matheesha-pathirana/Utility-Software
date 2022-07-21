import os
import time
import requests

try:
    pass
except ImportError:
    os.system('pip install requests')

url = "https://google.com"
try:
    response = requests.get(url)
    time.sleep(.4)
    input('Press enter to install Requirements\n')
    os.system('pip install -r requirements.txt')

except requests.exceptions.ConnectionError:
    input('You Need an Internet Connection!\npress enter to exit\n')
    exit()
