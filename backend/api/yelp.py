import requests

api_key = "E6pmD2fBselUP55r0L1eAru5pxapoYqPCknlDAvSAVgXMR3eZANI9nY_gfPkhs8Ibc69XblCvEfTx7qLeXBt1dufSMRsSmrV9HAkcWe8x6qHBsdX5wT6CEi7aIfaZXYx"
headers = {'Authorization': 'Bearer %s' % api_key}

BUSINESS_SEARCH_URL = 'https://api.yelp.com/v3/businesses/search'

def business_search(params):
    response = requests.get(BUSINESS_SEARCH_URL, headers=headers, params=params)
    return response

def business_details_search(ids: list[str]):
    responses = []
    for business_id in ids:
        business_details_url = 'https://api.yelp.com/v3/businesses/{business_id}'
        response = requests.get(business_details_search(business_details_url, 
                                headers=headers, params={"business_id_or_alias": business_id}))
        responses += response
    return responses
