import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2


class VideoPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Player")

        self.canvas = tk.Canvas(self.master)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.play_button = tk.Button(self.master, text="Play", command=self.play_video)
        self.play_button.pack(side="left", ipadx = 20, ipady = 10)

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_video)
        self.pause_button.pack(side="left", ipadx = 20, ipady = 10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_video)
        self.stop_button.pack(side="left", ipadx = 20, ipady = 10)

        self.video_path = None
        self.cap = None
        self.timer_id = None

    def play_video(self):
        if self.video_path is None:
            self.video_path = filedialog.askopenfilename(title="Select Video File",
                                                         filetypes=[("Video files", "*.mp4")])
            if not self.video_path:
                return

            self.cap = cv2.VideoCapture(self.video_path)

        self.timer_id = self.master.after(30, self.play_frame)

    def play_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)

            # Calculate the aspect ratio of the image
            width_ratio = self.canvas.winfo_width() / image.width
            height_ratio = self.canvas.winfo_height() / image.height
            ratio = min(width_ratio, height_ratio)

            # Resize the image to fit the canvas while maintaining aspect ratio
            new_width = int(image.width * ratio)
            new_height = int(image.height * ratio)
            image = image.resize((new_width, new_height))

            self.photo = ImageTk.PhotoImage(image=image)
            self.canvas.create_image(self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2, anchor=tk.CENTER, image=self.photo)
            self.timer_id = self.master.after(1, self.play_frame)
        else:
            self.stop_video()

    def pause_video(self):
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
            self.timer_id = None

    def stop_video(self):
        if self.cap:
            self.cap.release()
            self.cap = None
            self.video_path = None
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
            self.timer_id = None


def main():
    root = tk.Tk()
    root.geometry("1000x1000")
    video_player = VideoPlayer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
