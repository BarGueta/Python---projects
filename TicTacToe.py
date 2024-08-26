import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text="", font=("Arial", 20), width=6, height=3,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

    def on_button_click(self, i, j):
        if self.board[i][j] == "":
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner(i, j):
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_board()
            else:
                self.switch_player()

    def check_winner(self, i, j):
        # Check row
        if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.current_player:
            return True
        # Check column
        if self.board[0][j] == self.board[1][j] == self.board[2][j] == self.current_player:
            return True
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player or
                self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player):
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_board(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

# Example Usage:
root = tk.Tk()
root.resizable(False, False)
tic_tac_toe = TicTacToe(root)
root.mainloop()