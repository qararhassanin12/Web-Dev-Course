import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]

        self.buttons = [[tk.Button(self.window, text='', font=('Arial', 24), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                         for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == '' and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif all(self.board[i][j] != '' for i in range(3) for j in range(3)):
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True

        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != '':
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True

        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ''
                self.buttons[i][j].config(text='')

        self.current_player = 'X'

if __name__ == "__main__":
    game = TicTacToe()
    game.window.mainloop()
