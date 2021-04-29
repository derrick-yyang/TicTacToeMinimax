from tkinter import *
from tkinter import messagebox

t = Tk()
t.title('Tic-Tac-Toe')
t.configure(bg='white')
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

# X starts and is true
clicked = True
count = 0

# disabling buttons after win


def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# check if the board has a winner


def ifwon(board):
    global winner
    winner = False
    if (board[0][0] == board[0][1] == board[0][2] == "X" or board[1][0] == board[1][1] == board[1][2] == "X" or board[2][0] == board[2][1] == board[2][2] == "X" or
        board[0][0] == board[1][0] == board[2][0] == "X" or board[0][1] == board[1][1] == board[2][1] == "X" or board[0][2] == board[1][2] == board[2][2] == "X" or
            board[0][0] == board[1][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X"):

        winner = True
        messagebox.showinfo("Victory", "Player 1(X) Wins!")
        currplayer = Label(t, text="PLAYER 1(X) won", height=2,
                           font=("COMIC SANS MS", 10, "bold"), bg="white")
        currplayer.grid(row=0, column=0)
        disable_all_buttons()

    elif (board[0][0] == board[0][1] == board[0][2] == "O" or board[1][0] == board[1][1] == board[1][2] == "O" or board[2][0] == board[2][1] == board[2][2] == "O" or
          board[0][0] == board[1][0] == board[2][0] == "O" or board[0][1] == board[1][1] == board[2][1] == "O" or board[0][2] == board[1][2] == board[2][2] == "O" or
          board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O"):

        winner = True
        messagebox.showinfo("Victory", "Player 2(O) Wins!")
        currplayer = Label(t, text="PLAYER 2(O) won", height=2,
                           font=("COMIC SANS MS", 10, "bold"), bg="white")
        currplayer.grid(row=0, column=0)
        disable_all_buttons()

    elif count == 9:
        messagebox.showinfo("Draw", "It's a Draw!")
        currplayer = Label(t, text="Draw", height=2,
                           font=("COMIC SANS MS", 10, "bold"), bg="white")
        currplayer.grid(row=0, column=0)
        disable_all_buttons()


# if button is clicked
def b_click(b, x, y):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        board[x][y] = "X"
        ifwon(board)
        currplayer = Label(t, text="PLAYER 2(O)'s Move:", height=2,
                           font=("COMIC SANS MS", 10, "bold"), bg="white")
        currplayer.grid(row=0, column=0)
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        board[x][y] = "O"
        ifwon(board)
        currplayer = Label(t, text="PLAYER 1(X)'s Move:", height=2,
                           font=("COMIC SANS MS", 10, "bold"), bg="white")
        currplayer.grid(row=0, column=0)
    else:
        messagebox.showerror("Tic Tac Toe", "please select another box!")

# if reset button is clicked


def reset():
    global clicked, count, board
    global b1, b2, b3, b4, b5, b6, b7, b8, b9

    clicked = True
    count = 0
    currplayer = Label(t, text="PLAYER 1(X)'s Move:", height=2,
                       font=("COMIC SANS MS", 10, "bold"), bg="white")

    b1 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="black", fg="white", command=lambda: b_click(b1, 0, 0))
    b2 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="black", fg="white", command=lambda: b_click(b2, 0, 1))
    b3 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="black", fg="white", command=lambda: b_click(b3, 0, 2))

    b4 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="black", fg="white", command=lambda: b_click(b4, 1, 0))
    b5 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="black", fg="white", command=lambda: b_click(b5, 1, 1))
    b6 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="black", fg="white", command=lambda: b_click(b6, 1, 2))

    b7 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="black", fg="white", command=lambda: b_click(b7, 2, 0))
    b8 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="black", fg="white", command=lambda: b_click(b8, 2, 1))
    b9 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="black", fg="white", command=lambda: b_click(b9, 2, 2))

    reset_b = Button(t, text="Reset", font=("COMIC SANS MS", 10),
                     height=1, width=7, bg="gray85", command=lambda: reset())

    b1.grid(row=1, column=0)
    b2.grid(row=1, column=1)
    b3.grid(row=1, column=2)

    b4.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b6.grid(row=2, column=2)

    b7.grid(row=3, column=0)
    b8.grid(row=3, column=1)
    b9.grid(row=3, column=2)

    currplayer.grid(row=0, column=0)
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    reset_b.grid(row=0, column=1)


def TicTacToeGUI():
    global t
    reset_b = Button(t, text="Play Now", font=("COMIC SANS MS", 10),
                     height=1, width=7, bg="gray85", command=lambda: reset())

    b1 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="white")
    b2 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="white")
    b3 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="white")

    b4 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="white")
    b5 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="white")
    b6 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="white")

    b7 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="white")
    b8 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="white")
    b9 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                width=9, bg="white")

    reset_b.grid(row=0, column=1)

    b1.grid(row=1, column=0)
    b2.grid(row=1, column=1)
    b3.grid(row=1, column=2)

    b4.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b6.grid(row=2, column=2)

    b7.grid(row=3, column=0)
    b8.grid(row=3, column=1)
    b9.grid(row=3, column=2)

    t.mainloop()


TicTacToeGUI()
