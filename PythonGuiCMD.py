import tkinter as tk
from tkinter import scrolledtext
import subprocess

class PipGUI:
    def __init__(self, master):
        self.master = master
        master.title("CMD in python GUI")
        master.resizable(False, False)

        self.command_label = tk.Label(master, text="Enter pip command:")
        self.command_label.pack()

        self.command_entry = tk.Entry(master, width=50)
        self.command_entry.pack()

        self.run_button = tk.Button(master, text="Run Command", command=self.run_command)
        self.run_button.pack()

        self.output_text = scrolledtext.ScrolledText(master, height=10, width=50, bg="black", fg="white")
        self.output_text.pack()

    def run_command(self):
        command = self.command_entry.get()
        try:
            result = subprocess.run(command.split(), capture_output=True, text=True)
            output = result.stdout.strip()
            if output:
                self.output_text.insert(tk.END, output + "\n")
            error = result.stderr.strip()
            if error:
                self.output_text.insert(tk.END, error + "\n")
        except Exception as e:
            self.output_text.insert(tk.END, f"Error: {str(e)}\n")

def main():
    root = tk.Tk()
    app = PipGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
