import requests
import json

class BankAccount:
	def __init__():
		print('new obj')
	def __init__(self,  email_address, password, balance = 1756):
		self.email_address = email_address
		self.password = password
		self.balance = balance
	def deposit(self,amount):
		self.balance += amount
	def withdraw(self,amount):
		self.balance -= amount
	def GetPassword(self):
			return self.password
	def GetBalance(self):
			return self.balance