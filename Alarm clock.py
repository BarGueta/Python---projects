from tkinter import messagebox
import tkinter as tk
import datetime
import winsound

def check_alarm():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        winsound.Beep(1000, 1000)  # Beep sound for 2 seconds
        messagebox.showinfo("Time's up", "alarm for " + current_time)
    else:
        root.after(1000, check_alarm)  # Check again after 1 second

def set_alarm():
    global alarm_time
    alarm_time = entry.get()
    check_alarm()

root = tk.Tk()
root.title("Alarm Clock")
root.resizable(False, False)

label = tk.Label(root, text="Enter alarm time (HH:MM:SS):", font=("Helvetica", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 12))
entry.pack(pady=10)

button = tk.Button(root, text="Set Alarm", command=set_alarm, font=("Helvetica", 12))
button.pack(pady=10)

root.mainloop()
