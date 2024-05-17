from .dice_game import *
import os

def Cls():
	os.system('cls' if os.name == 'nt' else 'clear')

class UserManager:
	def __init__(self):
		self.user_list = {}

	def load_users(self):
		if not os.path.exists("users.txt"):
			with open('users.txt', 'w') as f:
				f.write("")
		else:
			with open('users.txt', 'r') as f:
				for line in f:
					values = line.strip().split(',')
					load_username = values[0]
					load_password = values[1]
					
					self.user_list[load_username] = User(load_username, load_password)


	def save_users(self):
		with open('users.txt', 'w') as f:
			for username, user in self.user_list.items():
				f.write(f"{user.username},{user.password}\n")
				
	def register(self):
		register_username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
		if len(register_username) >= 4:
			register_password = input("Enter username (at least 8 characters), or leave blank to cancel: ")
			if len(register_password) >= 8:
				if register_username not in self.user_list:
					self.user_list[register_username] = User(register_username, register_password)
					return
			else:
				input("Username must be at least 8 characters long...Enter to return")
				UserManager.register(self)
		elif register_username == "":
			return
				
		else:
			input("Username must be at least 4 characters long.")
			UserManager.register(self) 
		
	def login(self):
		print("Login Account")
		login_username = input("Username: ")
		login_password = input("Password: ")
		if login_username in self.user_list and login_password == self.user_list[login_username]:
			input("Account logged in successfully...")
			Cls()
		elif login_username or login_password == "":
			Cls()
			return
		else:
			input("Invalid username or password...Enter to continue")
			Cls()
			return