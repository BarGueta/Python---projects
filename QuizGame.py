import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")

        self.questions = {
            "What is the capital of France?": "Paris",
            "What is the largest mammal?": "Blue whale",
            "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
            "What is the chemical symbol for water?": "H2O"
        }

        self.score = 0
        self.total_questions = len(self.questions)
        self.current_question = None
        self.correct_answer = None

        self.question_label = tk.Label(self.master, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.master, font=("Arial", 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.score_label = tk.Label(self.master, text=f"Score: {self.score}/{self.total_questions}", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.ask_question()

    def ask_question(self):
        self.current_question = random.choice(list(self.questions.keys()))
        self.correct_answer = self.questions[self.current_question]
        self.question_label.config(text=self.current_question)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        if user_answer.lower() == self.correct_answer.lower():
            self.score += 1
            messagebox.showinfo("Correct", "Correct answer!")
            self.score_label.config(text=f"Score: {self.score}/{self.total_questions}")
            self.answer_entry.delete(0, 'end')
        else:
            messagebox.showerror("Incorrect", f"Incorrect answer! The correct answer is {self.correct_answer}")
            self.answer_entry.delete(0, 'end')

        if len(self.questions) > 1:
            del self.questions[self.current_question]
            self.ask_question()
        else:
            self.show_score()

    def show_score(self):
        messagebox.showinfo("Quiz Finished", f"Quiz finished!\nYour final score is: {self.score}/{self.total_questions}")
        self.master.quit()

def main():
    root = tk.Tk()
    quiz_game = QuizGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
