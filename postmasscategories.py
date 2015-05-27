import urllib2
import json
import sys
import random

if len(sys.argv) == 1 :
	print "Please provide an api host, for example 'https://s1409077295.bcapp.dev'"
	sys.exit(0)

url = str(sys.argv[1])
url = url + '/api/v3/catalog/categories'

count = 15

if len(sys.argv) == 3 :
	count = int(sys.argv[2])

for i in range(count):
	randomint = random.randint(0, sys.maxint)
	jsondata = json.dumps({"name": "Auto-Category " + `randomint`})
	urllib2.urlopen(url, jsondata)
