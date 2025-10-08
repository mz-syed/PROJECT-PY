# The program will prompt for a location, contact a web service and retrieve JSON for the web service
# and parse that data, and retrieve the first plus_code from the JSON

import urllib.request, urllib.parse, urllib.error
import json, ssl

api_service_url = 'https://py4e-data.dr-chuck.net/opengeo?'
print('===============================================================')
print('Geoapify Service URL -', api_service_url)
print('===============================================================')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("\nEnter the location (type 'quit' to quit service) : ")
    if address.lower() == 'quit':
        print('\nExiting Geoapify Service. Goodbye!')
        break

    address = address.strip()
    parameter = dict()
    parameter['q'] = address

    url = api_service_url + urllib.parse.urlencode(parameter)
    print('\nRetrieving -->', url)

    json_location_file = urllib.request.urlopen(url, context=ctx)
    data = json_location_file.read().decode()
    print('\nRetrieved', len(data), 'characters in JSON format', '{'+data[1:27]+'}')

    try:
        info = json.loads(data)
    except:
        info = None
    
    if not info:
        print('\n==== Failure To Retrieve ====')
        print(data)
        continue
    elif len(info['features']) < 1:
        print('\n==== No Data Found For This Location ====')
        continue

    plus_code = info['features'][0]['properties']['plus_code']
    location = info['features'][0]['properties']['formatted']
    print('\nPlus Code:', plus_code)
    print(location)








