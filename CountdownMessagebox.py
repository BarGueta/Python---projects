import time
import tkinter as tk
from tkinter import messagebox

def Start_count():
    print("Ok, The countdown from 10 begins!")

    for seconds in range(10, 0, -1):
        print(seconds, "s")
        time.sleep(1)
    messagebox.showinfo(title="10 seconds have passed...", message="Countdown has ended!")

root = tk.Tk()
root.title("Countdown with messagebox")
root.geometry("400x150")

button = tk.Button(root, text="Start countdown!",command=Start_count)
button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
