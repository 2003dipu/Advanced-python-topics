from tkinter import *
import random

class TicTacToe:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")

        self.players = ["x", "o"]
        self.player = random.choice(self.players)

        self.buttons = [[None] * 3 for _ in range(3)]
        self.label = Label(text=self.player + " turn", font=("consolas", 40), fg='#FF0000')
        self.label.pack(side=TOP)

        self.reset_button = Button(text="Restart", font=("Consolas", 20), fg='#00FF00', command=self.new_game)
        self.reset_button.pack(side=TOP)

        self.mode_button = Button(text="Switch Mode", font=("Consolas", 20), fg='#0000FF', command=self.switch_mode)
        self.mode_button.pack(side=TOP)

        self.frame = Frame(self.window)
        self.frame.pack()

        for row in range(3):
            for column in range(3):
                self.create_button(row, column)

        self.ai_player = self.player  # AI is "o"
        self.two_player_mode = True  # Default to AI mode

        self.two_player_mode_label = "Dual mode"
        self.ai_mode_label = "AI mode"
        self.label_text = self.two_player_mode_label

        self.new_game()

    def create_button(self, row, column):
        button = Button(self.frame, text="", font=("consolas", 40), height=2, width=5,
                        command=lambda row=row, column=column: self.next_turn(row, column))
        button.grid(row=row, column=column)
        self.buttons[row][column] = button

    def next_turn(self, row, column):
        if self.two_player_mode or (not self.two_player_mode and self.player == self.players[0]):
            if self.buttons[row][column]['text'] == "" and not self.check_winner():
                self.buttons[row][column]['text'] = self.player
                if self.check_winner():
                    self.label.config(text=f"{self.player} wins")
                elif self.count_empty_spaces() == 0:
                    self.label.config(text="Tie !")
                else:
                    self.player = self.players[1] if self.player == self.players[0] else self.players[0]
                    self.label.config(text=self.label_text)

                if not self.two_player_mode and self.player == self.ai_player:
                    self.ai_turn()

    def ai_turn(self):
        if self.player == self.ai_player and not self.check_winner():
            empty_cells = [(row, column) for row in range(3) for column in range(3) if
                           self.buttons[row][column]['text'] == ""]
        if empty_cells:
            row, column = random.choice(empty_cells)
            self.next_turn(row,column)

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                return True
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def count_empty_spaces(self):
        empty_count = sum(1 for row in self.buttons for button in row if button['text'] == "")
        return empty_count

    def new_game(self):
        self.player = random.choice(self.players)
        self.label_text = self.two_player_mode_label if self.two_player_mode else self.ai_mode_label
        self.label.config(text=f"{self.player}'s turn")
        for row in range(3):
            for column in range(3):
                self.buttons[row][column]['text'] = ""
                self.buttons[row][column].config(bg='#F0F0F0')

    def switch_mode(self):
        self.two_player_mode = not self.two_player_mode
        if self.two_player_mode:
            self.label_text = self.two_player_mode_label
        else:
            self.label_text = self.ai_mode_label
            if self.player == self.ai_player:
                self.ai_turn()

        self.label.config(text=self.label_text)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
