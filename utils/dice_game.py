import random
import os
import time
from utils.score import Score
from datetime import datetime

def Cls():
    os.system('cls' if os.name == 'nt' else 'clear')

class DiceGame:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.current_user = None
        self.scores = []
        self.load_scores()

    def load_scores(self):
        if not os.path.exists('data1'):
            os.makedirs('data1')
        if not os.path.exists('data1/rankings.txt'):
            open('data1/rankings.txt', 'w').close()
        else:
            with open('data1/rankings.txt', 'r') as file:
                for line in file:
                    username, game_id, points, wins = line.strip().split(',')
                    self.scores.append(Score(username, game_id, int(points), int(wins)))

    def save_scores(self):
        with open('data1/rankings.txt', 'w') as file:
            for score in self.scores:
                file.write(f"{score.username},{score.game_id},{score.points},{score.wins}\n")

    def roll_dice(self):
        print("Rolling the dice", end="", flush=True)
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.2)
        print()
        return random.randint(1, 6)

    def play_game(self):
        if self.current_user is None:
            input("No user is currently logged in.")
            return

        self.current_user.points = 0
        self.current_user.stages_won = 0

        while True:
            user_wins = 0
            cpu_wins = 0

            for _ in range(3):
                user_roll = self.roll_dice()
                cpu_roll = self.roll_dice()

                print(f"You rolled a {user_roll}. CPU rolled a {cpu_roll}.")
                if user_roll > cpu_roll:
                    user_wins += 1
                elif cpu_roll > user_roll:
                    cpu_wins += 1

                if user_wins == 2 or cpu_wins == 2:
                    break

            if user_wins > cpu_wins:
                self.current_user.points += 3
                self.current_user.stages_won += 1
                print("You won this stage!")
                print(f"Total Points: {self.current_user.points}")
                print(f"Stages Won: {self.current_user.stages_won}")
                choice = input("Enter 1 to continue to the next stage, 0 to stop: ")
                Cls()
                if choice == "0":
                    break
            else:
                input("Game over. You didn’t win any stages.")
                Cls()
                break

        if self.current_user.stages_won > 0:
            game_id = datetime.now().strftime("%Y%m%d%H%M%S%f")
            self.scores.append(Score(self.current_user.username, game_id, self.current_user.points, self.current_user.stages_won))
            self.scores.sort(key=lambda x: x.points, reverse=True)
            self.scores = self.scores[:10]
            self.save_scores()

    def show_top_scores(self):
        if not self.scores:
            input("No scores available yet.")
            Cls()
        else:
            print("Top 10 Scores:")
            for score in self.scores:
                print(f"Username: {score.username}, Game ID: {score.game_id}, Points: {score.points}, Stages Won: {score.wins}")
            input("")
            Cls()

    def logout(self):
        self.current_user = None
        Cls()

    def menu(self):
        while True:
            print(f"Welcome {self.user_manager.current_user.username}!")
            print("1. Start Game")
            print("2. Show Top Scores")
            print("3. Logout")
            choice = input("Enter: ")

            if choice == "1":
                self.play_game()
                Cls()
            elif choice == "2":
                self.show_top_scores()
            elif choice == "3":
                self.logout()
                Cls()
                break
            else:
                print("Invalid choice. Please try again.")
                Cls()
