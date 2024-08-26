import requests
import webbrowser
import tkinter as tk
from tkinter import messagebox

class RandomWikipediaViewer:
    def __init__(self, master):
        self.master = master
        master.title("Random Wikipedia Article Viewer")

        self.title_label = tk.Label(master, text="Random Wikipedia Article", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.summary_text = tk.Text(master, wrap="word", height=10, width=50)
        self.summary_text.pack(pady=10)

        self.fetch_button = tk.Button(master, text="Fetch Random Article", command=self.fetch_random_article)
        self.fetch_button.pack(pady=5)

        self.open_button = tk.Button(master, text="Open Article in Browser", command=self.open_article)
        self.open_button.pack(pady=5)

    def fetch_random_article(self):
        url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            title = data.get('title', 'Unknown Title')
            summary = data.get('extract', 'No summary available')
            self.summary_text.delete("1.0", "end")
            self.summary_text.insert("end", f"Title: {title}\n\n{summary}")
            self.article_url = data.get('content_urls', {}).get('desktop', {}).get('page', '#')
        else:
            messagebox.showerror("Error", "Failed to fetch random article.")

    def open_article(self):
        try:
            webbrowser.open(self.article_url)
        except AttributeError:
            messagebox.showerror("Error", "No article to open. Fetch an article first.")

def main():
    root = tk.Tk()
    app = RandomWikipediaViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
