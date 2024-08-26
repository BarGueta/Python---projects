import tkinter as tk
import random
from tkinter import messagebox

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman")

        self.words = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "lemon"]
        self.word = random.choice(self.words)
        self.guessed_letters = []
        self.attempts = 6

        self.word_display = tk.StringVar()
        self.word_display.set("_" * len(self.word))

        self.create_widgets()

    def create_widgets(self):
        self.word_label = tk.Label(self.master, textvariable=self.word_display, font=("Arial", 24))
        self.word_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        self.input_entry = tk.Entry(self.master, font=("Arial", 16))
        self.input_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.guess_button = tk.Button(self.master, text="Guess", font=("Arial", 16), command=self.guess_letter)
        self.guess_button.grid(row=1, column=3, padx=10, pady=10)

        self.remaining_attempts_label = tk.Label(self.master, text="Attempts left: 6", font=("Arial", 16))
        self.remaining_attempts_label.grid(row=1, column=4, padx=10, pady=10)

        self.input_entry.focus()

    def guess_letter(self):
        guess = self.input_entry.get().lower()
        self.input_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            tk.messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            tk.messagebox.showinfo("Already Guessed", "You've already guessed that letter.")
            return

        self.guessed_letters.append(guess)

        if guess not in self.word:
            self.attempts -= 1
            self.remaining_attempts_label.config(text=f"Attempts left: {self.attempts}")
            if self.attempts == 0:
                tk.messagebox.showinfo("Game Over", f"You ran out of attempts. The word was: {self.word}")
                self.master.destroy()
                return
        else:
            word_list = list(self.word_display.get())
            for index, letter in enumerate(self.word):
                if letter == guess:
                    word_list[index] = guess
            self.word_display.set("".join(word_list))

        if "_" not in self.word_display.get():
            tk.messagebox.showinfo("Congratulations!", f"You guessed the word: {self.word}")
            self.master.destroy()
            return


def main():
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()

# checks whether the current script is being run as the main program or being imported as a module into another script:
if __name__ == "__main__":
    main()
