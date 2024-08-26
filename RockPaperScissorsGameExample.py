import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock-Paper-Scissors Game")
        self.resizable(False, False)

        self.player_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.player_choice_label = tk.Label(self, text="Your Choice:")
        self.player_choice_label.grid(row=0, column=0, padx=10, pady=5)

        self.computer_choice_label = tk.Label(self, text="Computer's Choice:")
        self.computer_choice_label.grid(row=1, column=0, padx=10, pady=5)

        self.result_label = tk.Label(self, text="Result:")
        self.result_label.grid(row=2, column=0, padx=10, pady=5)

        self.player_choice_var = tk.StringVar()
        self.player_choice_var.set("")

        choices = ["Rock", "Paper", "Scissors"]

        for i, choice in enumerate(choices):
            button = tk.Button(self, text=choice, command=lambda ch=choice: self.play_game(ch))
            button.grid(row=0, column=i+1, padx=5, pady=5)

        self.player_score_label = tk.Label(self, text="Your Score: 0")
        self.player_score_label.grid(row=3, column=0, padx=10, pady=5)

        self.computer_score_label = tk.Label(self, text="Computer's Score: 0")
        self.computer_score_label.grid(row=4, column=0, padx=10, pady=5)

    def play_game(self, player_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        self.player_choice_var.set(player_choice)
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_label.config(text=f"Result: {result}")
        self.player_score_label.config(text=f"Your Score: {self.player_score}")
        self.computer_score_label.config(text=f"Computer's Score: {self.computer_score}")

        if self.player_score == 3:
            messagebox.showinfo("Game Over", "Congratulations! You win!")
            self.reset_game()
        elif self.computer_score == 3:
            messagebox.showinfo("Game Over", "Computer wins! Better luck next time.")
            self.reset_game()

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.player_choice_var.set("")
        self.computer_choice_label.config(text="Computer's Choice:")
        self.result_label.config(text="Result:")
        self.player_score_label.config(text="Your Score: 0")
        self.computer_score_label.config(text="Computer's Score: 0")

if __name__ == "__main__":
    app = RockPaperScissorsGame()
    app.mainloop()
