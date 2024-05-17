import os
from utils import user_manager

usermanager = user_manager.UserManager()

def Cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
        while True:
            print("Welcome to Dice Roll Game!")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            try:
                main_choice = input("Enter: ")
                Cls()
                if main_choice == "1":
                    usermanager.register()
                elif main_choice == "2":
                    usermanager.login()
                elif main_choice == "3":
                    exit()
                else:
                    raise Exception("Invalid choice. Please try again.")

            except Exception as e:
                print("Error: ", e)
                input("Enter to continue...")
                Cls()
                main()

if __name__ == "__main__":
     main()