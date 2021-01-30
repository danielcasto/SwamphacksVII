# This is written for PYTHON 3
# Don't forget to install requests package
import requests
import json

apiKey = '9e000d271e22e273a4b253ab8ee5b05d'
customerId = '60159ee54a4a860571284372'

def CreateUser():
	url = 'http://api.nessieisreal.com/customers?key={}'.format(apiKey)
	payload = {
	  "first_name": "Joe",
	  "last_name": "Shmoe",
	  "address": {
	    "street_number": "123",
	    "street_name": "Main Street",
	    "city": "Kissimmee",
	    "state": "FL",
	    "zip": "34746",
	    }
	 }

	# Create a Customer 
	response = requests.post( 
		url, 
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
		)

	if response.status_code == 201:
		return('customer created')
	else:
		return(response.status_code)

def CreateAccount():
	url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
	payload = {
	  "type": "Savings",
	  "nickname": "test",
	  "rewards": 10000,
	  "balance": 10000,	
	}
	# Create a Savings Account
	response = requests.post( 
		url, 
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
		)

	if response.status_code == 201:
		print('account created')
	else:
		print('nah')

CreateAccount();