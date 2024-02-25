import requests

api_key = "E6pmD2fBselUP55r0L1eAru5pxapoYqPCknlDAvSAVgXMR3eZANI9nY_gfPkhs8Ibc69XblCvEfTx7qLeXBt1dufSMRsSmrV9HAkcWe8x6qHBsdX5wT6CEi7aIfaZXYx"
headers = {'Authorization': 'Bearer %s' % api_key}

url = 'https://api.yelp.com/v3/businesses/search'
params = {'location': 'San Francisco', 'term': 'coffee'}

response = requests.get(url, headers=headers, params=params)

print(response.json())
