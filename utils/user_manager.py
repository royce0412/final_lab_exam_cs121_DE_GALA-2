from .dice_game import *  
import os

def Cls():
	os.system('cls' if os.name == 'nt' else 'clear')

class UserManager:
	def __init__(self):
		self.user_list = {}

	def load_users(self):
		if not os.path.exists("users.txt"):
			with open("users.txt", 'w') as f:
				f.write("")
		else:
			with open("users.txt", 'r') as f:
				for line in f:
					values = line.strip().split(',')
					if len(values) == 2:  # Ensure correct format
						load_username, load_password = values
						self.user_list[load_username] = load_password

	def save_users(self):
		with open("users.txt", 'w') as f:
			for username, password in self.user_list.items():
				f.write(f"{username},{password}\n")
				
	def register(self):
		while True:
			register_username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
			if not register_username:
				return
			if len(register_username) < 4:
				print("Username must be at least 4 characters long.")
				continue
			
			register_password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
			if not register_password:
				return
			if len(register_password) < 8:
				print("Password must be at least 8 characters long.")
				continue
			
			if register_username in self.user_list:
				print("Username already exists.")
			else:
				self.user_list[register_username] = register_password
				print("Registration successful!")
				self.save_users()  # Save the user list to users.txt
				return


	def validate_username_password(self, login_username, login_password):
		if not login_username or not login_password:
			return True
		
		if login_username not in self.user_list:
			print("Invalid username or password.")
			Cls()
			return False
			
		elif self.user_list[login_username] != login_password:
			print("Invalid password or password.")
			Cls()
			return False
		else:
			print("Logged in successfully!")
			return True

	def login(self):
		print("Login Account")
		while True:
			login_username = input("Username: ")
			login_password = input("Password: ")
			if self.validate_username_password(login_username, login_password):
				return
