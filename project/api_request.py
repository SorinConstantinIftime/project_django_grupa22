import requests
import json

# url = "http://127.0.0.1:8000/api/api/"
# payload = json.dumps({
#     "city": "Timisoara",
#     "country": "Romania"
# })
# headers = {
#     "Content-Type": "application/json"
# }
# response = requests.request("GET", url, headers=headers, data=payload)
# print(response.json())
#
# ------------------------------------
# url = "http://127.0.0.1:8000/api/api/4/"
# payload = json.dumps({
#     "city": "Timisoara1",
#     "country": "Romania"
# })
# headers = {
#     "Content-Type": "application/json"
# }
# response = requests.request("PUT", url, headers=headers, data=payload)
# print(response.json())

# url = "http://127.0.0.1:8000/api/api/4/"
# payload = json.dumps({
#     "city": "Timisoara1",
#     "country": "Romania"
# })
# headers = {
#     "Content-Type": "application/json"
# }
# response = requests.request("DELETE", url, headers=headers, data=payload)
# print(response.json())

import requests

url = "https://v6.exchangerate-api.com/v6/9e07f2ee0dd1746ff4b28fad/latest/RON"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json()["conversion_rates"]["EUR"])