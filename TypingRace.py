import tkinter as tk
import random


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("500x400")

        self.words = ["python", "java", "javascript", "ruby", "html", "css", "php", "swift", "kotlin"]
        self.current_word = ""
        self.score = 0
        self.time_left = 15

        self.word_label = tk.Label(self.root, text="", font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.input_entry = tk.Entry(self.root, font=("Arial", 18))
        self.input_entry.pack(pady=10)
        self.input_entry.bind("<Return>", self.check_word)

        self.timer_label = tk.Label(self.root, text="Time left: 15", font=("Arial", 16))
        self.timer_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 16))
        self.score_label.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

    def start_game(self):
        self.start_button.config(state="disabled")
        self.new_word()
        self.root.after(1000, self.countdown)

    def new_word(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)
        self.input_entry.delete(0, tk.END)

    def check_word(self, event):
        user_input = self.input_entry.get().strip()
        if user_input == self.current_word:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.new_word()
        self.input_entry.delete(0, tk.END)

    def countdown(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.root.after(1000, self.countdown)
        else:
            self.timer_label.config(text="Time's up!")
            self.input_entry.config(state="disabled")
            self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
            self.restart_button.pack(pady=10)

    def restart_game(self):
        self.score = 0
        self.time_left = 15
        self.score_label.config(text=f"Score: {self.score}")
        self.timer_label.config(text=f"Time left: {self.time_left}")
        self.input_entry.config(state="normal")
        self.input_entry.focus()
        self.restart_button.destroy()
        self.new_word()
        self.start_button.config(state="normal")


def main():
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()


if __name__ == "__main__":
    main()
