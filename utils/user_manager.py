import os
from utils.user import User

def Cls():
    os.system('cls' if os.name == 'nt' else 'clear')

class UserManager:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.load_users()

    def load_users(self):
        if not os.path.exists('data1'):
            os.makedirs('data1')
        if not os.path.exists('data1/users.txt'):
            open('data1/users.txt', 'w').close()
        else:
            with open('data1/users.txt', 'r') as file:
                for line in file:
                    username, password = line.strip().split(',')
                    self.users[username] = User(username, password)

    def save_users(self):
        with open('data1/users.txt', 'w') as file:
            for user in self.users.values():
                file.write(f"{user.username},{user.password}\n")

    def validate_username(self, username):
        if len(username) < 4:
            raise Exception("Username must be at least 4 characters long.")
        if username in self.users:
            raise Exception("Username already exists.")
        return True

    def validate_password(self, password):
        if len(password) < 8:
            raise Exception("Password must be at least 8 characters long.")
        return True

    def register(self):
        try:
            username = input("Enter username (leave blank to cancel): ")
            if not username:
                return
            self.validate_username(username)

            password = input("Enter password (leave blank to cancel): ")
            if not password:
                return
            self.validate_password(password)

            self.users[username] = User(username, password)
            self.save_users()
            print("Registration successful!")
        except Exception as e:
            print("Error: ", e)
        input("Enter to continue...")
        Cls()

    def login(self):
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")

            if username in self.users and self.users[username].password == password:
                input(f"Login successful! Welcome, {username}.")
                Cls()
                self.current_user = self.users[username]
                return True
            else:
                raise Exception("Invalid username or password.")
        except Exception as e:
            print("Error: ", e)
        input("Enter to continue...")
        Cls()
        return False
