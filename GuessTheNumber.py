import tkinter as tk
from tkinter import messagebox
import random


class NumberGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guessing Game")
        self.geometry("300x150")

        self.secret_number = random.randint(1, 100)
        self.remaining_attempts = 5

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Guess the secret number (between 1 and 100):")
        self.label.pack(pady=5)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get()
        try:
            guess = int(guess)
            self.remaining_attempts -= 1
            if guess < self.secret_number:
                messagebox.showinfo("Result", "Too low! Try again.")
            elif guess > self.secret_number:
                messagebox.showinfo("Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Result", f"Congratulations! You guessed the number {self.secret_number}!")
                self.restart_game()
            if self.remaining_attempts == 0:
                messagebox.showinfo("Result",
                                    f"Sorry! You have used all 5 attempts. The secret number was {self.secret_number}.")
                self.restart_game()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.remaining_attempts = 5
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    app = NumberGuessingGame()
    app.mainloop()
