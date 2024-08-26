import tkinter as tk
from tkinter import messagebox

class CalorieTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Calorie Tracker")
        self.meal_entries = []

        self.meal_frame = tk.Frame(self.root)
        self.meal_frame.pack(padx=10, pady=10)

        self.add_meal_button = tk.Button(self.meal_frame, text="Add Meal", command=self.add_meal)
        self.add_meal_button.grid(row=0, column=0, padx=5, pady=5)

        self.plan_meals_button = tk.Button(self.meal_frame, text="Plan Meals", command=self.plan_meals)
        self.plan_meals_button.grid(row=0, column=1, padx=5, pady=5)

        self.grocery_list_button = tk.Button(self.meal_frame, text="Generate Grocery List", command=self.generate_grocery_list)
        self.grocery_list_button.grid(row=0, column=2, padx=5, pady=5)

    def add_meal(self):
        meal_window = tk.Toplevel(self.root)
        meal_window.title("Add Meal")

        meal_label = tk.Label(meal_window, text="Meal:")
        meal_label.grid(row=0, column=0, padx=5, pady=5)

        meal_entry = tk.Entry(meal_window)
        meal_entry.grid(row=0, column=1, padx=5, pady=5)

        calorie_label = tk.Label(meal_window, text="Calories:")
        calorie_label.grid(row=1, column=0, padx=5, pady=5)

        calorie_entry = tk.Entry(meal_window)
        calorie_entry.grid(row=1, column=1, padx=5, pady=5)

        save_button = tk.Button(meal_window, text="Save", command=lambda: self.save_meal(meal_entry.get(), calorie_entry.get(), meal_window))
        save_button.grid(row=2, column=1, padx=5, pady=5)

        self.meal_entries.append((meal_entry, calorie_entry))

    def save_meal(self, meal, calories, meal_window):
        if meal and calories:
            self.meal_entries.append((meal, calories))
            messagebox.showinfo("Success", "Meal saved successfully!")
            meal_window.destroy()
        else:
            messagebox.showerror("Error", "Please enter meal and calories!")

    def plan_meals(self):
        if self.meal_entries:
            plan_window = tk.Toplevel(self.root)
            plan_window.title("Planned Meals")

            for i, (meal, calories) in enumerate(self.meal_entries):
                meal_label = tk.Label(plan_window, text=f"{i + 1}. {meal}: {calories} calories")
                meal_label.pack(padx=5, pady=2)
        else:
            messagebox.showerror("Error", "No meals added yet!")

    def generate_grocery_list(self):
        if self.meal_entries:
            grocery_list_window = tk.Toplevel(self.root)
            grocery_list_window.title("Grocery List")

            grocery_list_label = tk.Label(grocery_list_window, text="Grocery List:")
            grocery_list_label.pack(padx=5, pady=2)

            grocery_list_text = "\n".join([f"- {meal} ({calories} calories)" for meal, calories in self.meal_entries])
            grocery_list_textbox = tk.Text(grocery_list_window, height=10, width=50)
            grocery_list_textbox.insert(tk.END, grocery_list_text)
            grocery_list_textbox.pack(padx=5, pady=5)
            grocery_list_textbox.config(state="disabled")
        else:
            messagebox.showerror("Error", "No meals added yet!")

def main():
    root = tk.Tk()
    app = CalorieTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
