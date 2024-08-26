# Calendar app:

import calendar
import tkinter as tk

def show_calendar(year, month):
    # Create a calendar object
    cal = calendar.monthcalendar(year, month)
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    # Clear any existing widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Add labels for weekdays
    for col, weekday in enumerate(weekdays):
        label = tk.Label(frame, text=weekday)
        label.grid(row=0, column=col, padx=5, pady=5)

    # Add labels for each day in the month
    for week_num, week in enumerate(cal):
        for day_num, day in enumerate(week):
            if day != 0:
                label = tk.Label(frame, text=str(day))
                label.grid(row=week_num + 1, column=day_num, padx=5, pady=5)

# Create main window
root = tk.Tk()
root.title("Calendar App")
root.resizable(False, False)

# Create frame for calendar display
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create labels and entry for year and month
year_label = tk.Label(root, text="Year:")
year_label.pack(side=tk.LEFT)
year_entry = tk.Entry(root)
year_entry.pack(side=tk.LEFT)

month_label = tk.Label(root, text="Month (1-12):")
month_label.pack(side=tk.LEFT)
month_entry = tk.Entry(root)
month_entry.pack(side=tk.LEFT)

# Button to show calendar
show_button = tk.Button(root, text="Show Calendar", command=lambda: show_calendar(int(year_entry.get()), int(month_entry.get())))
show_button.pack()

root.mainloop()
