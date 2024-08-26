import tkinter as tk
import time


class DigitalClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Digital Clock")

        self.time_label = tk.Label(self.master, font=('Arial', 50), bg='black', fg='green')
        self.time_label.pack()

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.master.after(1000, self.update_clock)  # (after how much time to update the clock in ms)

def main():
    root = tk.Tk()
    root.resizable(False, False)
    digital_clock = DigitalClock(root)
    root.mainloop()


if __name__ == "__main__":
    main()
