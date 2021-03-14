import v20 

API = "api-fxtrade.oanda.com"
STR_API = "stream-fxtrade.oanda.com"

ACCESS_TOKEN = "89b68cfce2029fae762a5f3253395e25-e7f04638aab06da3d8b9de4de07c1826"
ID = "101-004-4838689-002"


api = v20.Context(hostname=API, token=ACCESS_TOKEN, port=433)
stream_api = v20.Context(hostname=STR_API, token=ACCESS_TOKEN, port=433)

response = api.pricing.get(accountID=ID, instruments="USD_CAD")

print(json.loads(response.body['prices'][0].json()))