import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("400x150")
        self.root.resizable(False, False)

        self.height_label = tk.Label(root, text="Enter your height (cm):")
        self.height_label.pack()

        self.height_entry = tk.Entry(root)
        self.height_entry.pack()

        self.weight_label = tk.Label(root, text="Enter your weight (kg):")
        self.weight_label.pack()

        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()

        self.calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack()

    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            bmi = weight / ((height / 100) ** 2)
            messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid height and weight.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
