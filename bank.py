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
account.GetBalance()