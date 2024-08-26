import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.expression = ""
        self.input_var = tk.StringVar()
        self.input_var.set("")
        self.entry = tk.Entry(master, textvariable=self.input_var, justify="right", font=("Arial", 20))
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)  # Added Clear button
        ]
        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.expression))
                self.input_var.set(result)
                self.expression = result
            except:
                self.input_var.set("Error")
                self.expression = ""
        elif text == "C":  # Clear button
            self.input_var.set("")
            self.expression = ""
        else:
            self.expression += text
            self.input_var.set(self.expression)

# Example Usage:
root = tk.Tk()
root.resizable(False, False)
calculator = Calculator(root)
root.mainloop()
