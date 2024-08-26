import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master, width=1000, height=1000, cell_size=20, score_count=0):
        self.master = master
        self.master.title("Snake Game")

        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid_width = self.width // self.cell_size
        self.grid_height = self.height // self.cell_size

        self.score_count = score_count
        self.score = tk.Label(self.master, bg="white", foreground="black", text="Score: " + str(self.score_count), font=('Arial', 15))
        self.score.pack()

        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        self.press_arrow_keys = tk.Label(self.canvas, bg="black", foreground="white", text="Press any arrow key to start", font=('Arial', 15))

        self.press_arrow_keys.place(relx = 0.5, rely = 0.5, anchor="center")

        self.gameover = tk.Label(self.canvas, bg="black", foreground="red", text="Game over!", font=('Arial', 20))

        self.snake = [(self.grid_width // 2, self.grid_height // 2)]
        self.direction = (0, 0)  # Initially stationary
        self.food = self.generate_food()

        self.master.bind("<KeyPress>", self.on_key_press)

        self.draw()

    def on_key_press(self, event):
        key = event.keysym
        if key == "Up" and self.direction != (0, 1):  # Avoid moving downwards when pressing Up
            self.direction = (0, -1)
            self.press_arrow_keys.place_forget()
        elif key == "Down" and self.direction != (0, -1):  # Avoid moving upwards when pressing Down
            self.direction = (0, 1)
            self.press_arrow_keys.place_forget()
        elif key == "Left" and self.direction != (1, 0):  # Avoid moving rightwards when pressing Left
            self.direction = (-1, 0)
            self.press_arrow_keys.place_forget()
        elif key == "Right" and self.direction != (-1, 0):  # Avoid moving leftwards when pressing Right
            self.direction = (1, 0)
            self.press_arrow_keys.place_forget()

    def generate_food(self):
        while True:
            food = (random.randint(0, self.grid_width - 1), random.randint(0, self.grid_height - 1))
            if food not in self.snake:
                return food

    def move_snake(self):
        head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])

        if head == self.food:
            self.snake.insert(0, head)
            self.food = self.generate_food()
            self.score_count += 1
            self.score.config(text="Score: " + str(self.score_count))
        else:
            self.snake.pop()
            self.snake.insert(0, head)

        # Check if the snake hits the wall or itself
        if (head[0] < 0 or head[0] >= self.grid_width or
            head[1] < 0 or head[1] >= self.grid_height or
            head in self.snake[1:]):
            self.master.unbind("<KeyPress>")
            self.gameover.place(relx=0.5,rely=0.5,anchor="center")

    def draw(self):
        self.canvas.delete("all")

        # Draw food
        self.canvas.create_rectangle(self.food[0] * self.cell_size, self.food[1] * self.cell_size,
                                     (self.food[0] + 1) * self.cell_size, (self.food[1] + 1) * self.cell_size,
                                     fill="red")

        # Draw snake
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0] * self.cell_size, segment[1] * self.cell_size,
                                         (segment[0] + 1) * self.cell_size, (segment[1] + 1) * self.cell_size,
                                         fill="green")

    def update(self):
        self.move_snake()
        self.draw()
        self.master.after(100, self.update)

def main():
    root = tk.Tk()
    root.resizable(False, False)
    game = SnakeGame(root)
    game.update()
    root.mainloop()

if __name__ == "__main__":
    main()
