import tkinter as tk
import random

class DiceRollerApp:
    def __init__(self, master):
        self.master = master
        master.title("Dice Rolling Simulator")
        master.geometry("300x300")
        master.resizable(False, False)

        self.result_label = tk.Label(master, text="Roll the dice!", font=("Helvetica", 24))
        self.result_label.pack(pady=20)

        self.roll_button = tk.Button(master, text="Roll Dice", command=self.roll_dice, font=("Helvetica", 16))
        self.roll_button.pack()

        self.dice_label = tk.Label(master, font=("Helvetica", 72), padx=20, pady=20)
        self.dice_label.pack()

    def roll_dice(self):
        roll_result = random.randint(1, 6)
        self.result_label.config(text=f"You rolled: {roll_result}")
        self.display_dice(roll_result)

    def display_dice(self, value):
        dice_shapes = [
            "",                            # 0
            "⚀", "⚁", "⚂", "⚃", "⚄", "⚅"  # 1 to 6
        ]
        self.dice_label.config(text=dice_shapes[value])

def main():
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
