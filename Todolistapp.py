import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        view_tasks()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        index = int(selected_task_index[0])
        del tasks[index]
        view_tasks()

def clear_tasks():
    tasks.clear()
    view_tasks()

def view_tasks():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

root = tk.Tk()
root.title("Todo List")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_task = tk.Label(frame, text="Task:")
label_task.grid(row=0, column=0)

entry_task = tk.Entry(frame, width=30)
entry_task.grid(row=0, column=1)

button_add = tk.Button(frame, text="Add Task", command=add_task)
button_add.grid(row=0, column=2, padx=5)

button_remove = tk.Button(frame, text="Remove Task", command=remove_task)
button_remove.grid(row=1, column=0, pady=10)

button_clear = tk.Button(frame, text="Clear All Tasks", command=clear_tasks)
button_clear.grid(row=2, column=0, pady=10)

task_list = tk.Listbox(frame, width=40)
task_list.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
