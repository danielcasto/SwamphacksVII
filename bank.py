import requests
import json

class BankAccount:
	def __init__(self,  email_address, password, name, address, state, zipcode, balance = 0):
		self.email_address = email_address
		self.__password = password
		self.name = name
		self.address = address
		self.state = state
		self.zipcode = zipcode
		self.__balance = balance
	def deposit(self,amount):
		self.balance += amount
	def withdraw(self,amount):
		self.balance -= amount
	def GetPassword(self):
			return self.__password
	def GetBalance(self):
			return self.__balance

account = BankAccount("Michaelmendez@mail.com", "password", "Michael Mendez",'3709 Eagle Isle Circle','Florida', 34746)

# Unused API Code
#def CreateUser():
	#apiKey = '9e000d271e22e273a4b253ab8ee5b05d'

	#url = 'http://api.nessieisreal.com/customers?key={}'.format(apiKey)
	#payload = {
	  #"first_name": "Bobby Shmurda",
	  #"last_name": "Shmoe",
	  #"address": {
	    #"street_number": "123",
	    #"street_name": "Main Street",
	    #"city": "Jail",
	    #"state": "CA",
	   # "zip": "12345",
	  #  }
	 #}

	# Create a Customer 
	#response = requests.post( 
		#url, 
		#data=json.dumps(payload),
		#headers={'content-type':'application/json'},
	#)

	#if response.status_code == 201:
		#print('customer created')
	#else:
		#print(response.status_code)

#def CreateAccount():
	#apiKey = '9e000d271e22e273a4b253ab8ee5b05d'
	#customerId = '60159bff4a4a86057128436f'

	#url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
	#payload = {
  		#"type": "Checking",
  		#"nickname": "string",
 		#"rewards": 0,
  		#"balance": 0,
  		#"account_number": "1234567812345678",
  	#}

	# Create a Savings Account
	#response = requests.post( 
	#	url, 
	#	data=json.dumps(payload),
	#	headers={'content-type':'application/json'},
	#)

	#if response.status_code == 201:
	#	print('account created')
	#else:
	#	print(response.status_code)