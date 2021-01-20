import requests
import json

print(requests.__version__) #print version of requests

response = requests.get("https://www.google.ca", timeout = 30)#get google homepage
#print(response.status_code)
