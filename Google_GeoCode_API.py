import json
import urllib

base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
geocode_key = "AIzaSyCTeRotwFNRPbd8fgFwNbDUMdqTWP6I1rI"

while True:
    Location_requested = raw_input("Please enter the Location - ")
    if len(Location_requested) < 1:
        break

    params = urllib.urlencode({'sensor': 'false', 'address': Location_requested, 'key': geocode_key})

    final_url = base_url + params

    print "Reading URL: \"" + final_url + "\""

    data = urllib.urlopen(final_url)
    dj = data.read()                 #here we have a JSON object, not file-like object because we didn't read from file!!

    print "We read %s characters" % len(dj)

    data_json = json.loads(dj)

    print data_json['status']
    print json.dumps(data_json['results'][0]['geometry'], indent=4)

    if data_json['status'] == "OK":
        print "The result is ok"

    header = data.info().dict

    print "Header is: " + json.dumps(header, indent=6)