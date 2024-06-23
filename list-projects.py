# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://vijayk12101.atlassian.net/rest/api/3/project"

API_TOKEN = ""

auth = HTTPBasicAuth("vijay.k.12101@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

for i in range(len(output)):
    print(output[i]["name"])

