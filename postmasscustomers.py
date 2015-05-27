import urllib2
import json
import sys
import random
import base64


def main():

	if len(sys.argv) == 1 :
		print "Usage:"
		print "Please provide an api host, for example 'https://s1409077295.bcapp.dev'"
		print "create a legacy api user and token"
		print sys.argv[0] + " <API_Host> <API_UserName> <APIToken>"
		sys.exit(0)

	url = str(sys.argv[1])
	url = url + '/api/v2/customers'

	user = str(sys.argv[2])
	token = str(sys.argv[3])

	count = 30

	if len(sys.argv) == 3 :
		count = int(sys.argv[2])

	for i in range(count):
		randomint = random.randint(0, sys.maxint)
		jsondata = createRandomCustomer()
		createConnection(url, user, token, jsondata)


def createRandomCustomer() :
	firstName = randomString()
	lastName = randomString()
	customer = {
		"first_name":firstName,
		"last_name":lastName,
		"email": firstName + "." + lastName + "@example.com"
	}
	jsondata = json.dumps(customer)
	return jsondata


def createConnection(url , user, token, data) :
	request = urllib2.Request(url)
	# You need the replace to handle encodestring adding a trailing newline
	# (https://docs.python.org/2/library/base64.html#base64.encodestring)
	base64string = base64.encodestring('%s:%s' % (user, token)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % base64string)
	request.add_header("Content-Type","application/json")
	result = urllib2.urlopen(request,data)

def randomString() :
	return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(8))

main()
