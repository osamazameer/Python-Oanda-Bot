import json
from oandav20 import API
from oandav20.exceptions import V20error
# from oandav20.endpoints.accounts as accounts
# from oandav20.endpoints.trades as trades
# from oandav20.endpoints.pricing as pricing

ACCESS_TOKEN = "89b68cfce2029fae762a5f3253395e25-e7f04638aab06da3d8b9de4de07c1826"
ID = "101-004-4838689-002"
client = API(access_token=ACCESS_TOKEN)

lor = []
lor.append(trade)