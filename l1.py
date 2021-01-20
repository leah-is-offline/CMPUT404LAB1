import requests
import json

print(requests.__version__) #print version of requests

response = requests.get("https://www.google.ca", timeout = 30)#get google homepage
print(response.status_code)

url = "https://raw.githubusercontent.com/leah-is-offline/CMPUT404LAB1/master/l1.py"
response = requests.get(url)
print(response.text)
