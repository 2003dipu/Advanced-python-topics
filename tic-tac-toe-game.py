from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+"'s turn"))
            elif check_winner() is True:
                label.config(text=(players[0]+' wins'))
            elif check_winner() == "Tie":
                label.config(text="Tie !")
        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+"'s turn"))
            elif check_winner() is True:
                label.config(text=(players[1]+' wins'))
            elif check_winner() == "Tie":
                label.config(text="Tie !")

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg='#00FFFF') # #00FFFF = the color is Cyan
            buttons[row][1].config(bg='#00FFFF')
            buttons[row][2].config(bg='#00FFFF')
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg='#00FFFF')
            buttons[1][column].config(bg='#00FFFF')
            buttons[2][column].config(bg='#00FFFF')
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg='#00FFFF')
        buttons[1][1].config(bg='#00FFFF')
        buttons[2][2].config(bg='#00FFFF')
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg='#00FFFF')
        buttons[1][1].config(bg='#00FFFF')
        buttons[2][0].config(bg='#00FFFF')
        return True
    elif count_empty_spaces() == 0:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='#FF8C00') # this color is orange
        return "Tie"
    else:
        return False

def count_empty_spaces():
    spaces = 9
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    return spaces

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player +"'s turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg='#F0F0F0')

window = Tk()
window.title("Tic-Tac-Toe")

players = ["x", "o"]
player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
label = Label(text=player + " turn", font=("consolas", 40))
label.pack(side=TOP)
reset_button = Button(text="restart", font=("Consolas", 20), command=new_game)
reset_button.pack(side=TOP)
frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("consolas", 40), height=2, width=5,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)
        
window.mainloop()
