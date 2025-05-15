import requests
import json


base_url="https://rickandmortyapi.com/api/" 
endpoint="character"

r =requests.get(base_url+endpoint)

print(r.json()["info"])
print(r)
print(requests.get(base_url+'lion'))