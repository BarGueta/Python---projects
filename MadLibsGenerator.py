import tkinter as tk

class MadLibsGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Mad Libs Generator")
        master.resizable(False, False)

        self.story_label = tk.Label(master, text="Enter words for your story:", font=("Helvetica", 16))
        self.story_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.noun_label = tk.Label(master, text="Noun:")
        self.noun_label.grid(row=1, column=0, sticky="e", padx=5)
        self.noun_entry = tk.Entry(master, width=30)
        self.noun_entry.grid(row=1, column=1, padx=5, pady=5)

        self.verb_label = tk.Label(master, text="Verb:")
        self.verb_label.grid(row=2, column=0, sticky="e", padx=5)
        self.verb_entry = tk.Entry(master, width=30)
        self.verb_entry.grid(row=2, column=1, padx=5, pady=5)

        self.adjective_label = tk.Label(master, text="Adjective:")
        self.adjective_label.grid(row=3, column=0, sticky="e", padx=5)
        self.adjective_entry = tk.Entry(master, width=30)
        self.adjective_entry.grid(row=3, column=1, padx=5, pady=5)

        self.generate_button = tk.Button(master, text="Generate Mad Libs", command=self.generate_story)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.generated_story_label = tk.Label(master, text="", font=("Helvetica", 12), wraplength=400, justify="left")
        self.generated_story_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def generate_story(self):
        noun = self.noun_entry.get()
        verb = self.verb_entry.get()
        adjective = self.adjective_entry.get()

        if not noun or not verb or not adjective:
            self.generated_story_label.config(text="Please fill in all the fields.")
            return

        story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb}.\n"
        story += f"But one day, the {noun} wanted to {verb} so much that it caused chaos!\n"
        story += f"Everyone had to {verb} to save the day.\n"
        story += f"And they all had a {adjective} life after that."

        self.generated_story_label.config(text=story)

def main():
    root = tk.Tk()
    app = MadLibsGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
