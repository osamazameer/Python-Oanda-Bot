import requests
import  json
import  numpy as np
import pandas as pd


API = "api-fxtrade.oanda.com"
STR_API = "stream-fxtrade.oanda.com"

ACCESS_TOKEN = "e7a67beaece6210fbda1b87d3425f6f9-a09edd6a08c36193a70dc9c373162d58"
ID = "101-004-4838689-002"


# path = f"/v3/accounts/{ID}/pricing"
path = f"/v3/accounts/{ID}"
query = {"instruments":"GBP_USD"}
headers = {"Authorization": "Bearer e7a67beaece6210fbda1b87d3425f6f9-a09edd6a08c36193a70dc9c373162d58"}
# response = requests.get("https://"+ API + path, headers=headers, params=query)


response = requests.get("https://"+ API + path, headers=headers, params=query)

# response.json()
print(response.json())