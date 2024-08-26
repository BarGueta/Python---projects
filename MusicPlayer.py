import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x100")

        pygame.init()
        pygame.mixer.init()

        self.current_song = tk.StringVar()
        self.song_label = tk.Label(root, textvariable=self.current_song)
        self.song_label.pack(ipadx=5,ipady=5)

        frame = tk.Frame()
        frame.pack()

        self.play_button = tk.Button(frame, text="Play", command=self.play_music, padx=5, pady=5)
        self.play_button.grid(row=1,column=1,ipadx=5,ipady=5)

        self.stop_button = tk.Button(frame, text="Stop", command=self.stop_music, padx=5, pady=5)
        self.stop_button.grid(row=1,column=2,ipadx=5,ipady=5)

        self.load_button = tk.Button(frame, text="Load Music", command=self.load_music, padx=5, pady=5)
        self.load_button.grid(row=1,column=3,ipadx=5,ipady=5)

    def load_music(self):
        filename = filedialog.askopenfilename()
        pygame.mixer.music.load(filename)
        self.current_song.set("Now Playing: " + filename)

    def play_music(self):
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
