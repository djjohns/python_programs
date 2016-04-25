import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + '?' + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    #uncomment to print json results
    #print json.dumps(js, indent=4)
    json.dumps(js, indent=4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    location = js['results'][0]['formatted_address']
    placeID = js ['results'][0]['place_id']
    print 'place_id:', placeID
    print 'Location:', location
    print 'lat',lat,'lng',lng

