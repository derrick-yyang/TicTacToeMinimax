from tkinter import *
from tkinter import messagebox


class game(object):

    def __init__(self, t):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.count = 0
        self.clicked = True # If true, X is clicking. If False, O is clicking

        self.reset_b = Button(t, text="Play Now", font=("COMIC SANS MS", 10),
                              height=1, width=7, bg="gray85", command=lambda: self.reset(t))

        self.b1 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="white")
        self.b2 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="white")
        self.b3 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="white")

        self.b4 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="white")
        self.b5 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="white")
        self.b6 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="white")

        self.b7 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="white")
        self.b8 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="white")
        self.b9 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="white")

        self.currplayer = Label(t, text="Click the Play Button:", height=2,
                                font=("COMIC SANS MS", 10, "bold"), bg="white")

    def showBoard(self):

        self.b1.grid(row=1, column=0)
        self.b2.grid(row=1, column=1)
        self.b3.grid(row=1, column=2)

        self.b4.grid(row=2, column=0)
        self.b5.grid(row=2, column=1)
        self.b6.grid(row=2, column=2)

        self.b7.grid(row=3, column=0)
        self.b8.grid(row=3, column=1)
        self.b9.grid(row=3, column=2)

        self.currplayer.grid(row=0, column=0)
        self.reset_b.grid(row=0, column=1)

    def reset(self, t):
        self.clicked = True
        self.count = 0
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.currplayer = Label(t, text="PLAYER 1(X)'s Move:", height=2,
                                font=("COMIC SANS MS", 10, "bold"), bg="white")

        self.b1 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="black", fg="white", command=lambda: self.b_click(self.b1, 0, 0, t))
        self.b2 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="black", fg="white", command=lambda: self.b_click(self.b2, 0, 1, t))
        self.b3 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="black", fg="white", command=lambda: self.b_click(self.b3, 0, 2, t))

        self.b4 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="black", fg="white", command=lambda: self.b_click(self.b4, 1, 0, t))
        self.b5 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="black", fg="white", command=lambda: self.b_click(self.b5, 1, 1, t))
        self.b6 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="black", fg="white", command=lambda: self.b_click(self.b6, 1, 2, t))

        self.b7 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="black", fg="white", command=lambda: self.b_click(self.b7, 2, 0, t))
        self.b8 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="black", fg="white", command=lambda: self.b_click(self.b8, 2, 1, t))
        self.b9 = Button(t, text=" ", font=("COMIC SANS MS", 20), height=3,
                         width=9, bg="black", fg="white", command=lambda: self.b_click(self.b9, 2, 2, t))

        self.reset_b = Button(t, text="Reset", font=("COMIC SANS MS", 10),
                              height=1, width=7, bg="gray85", command=lambda: self.reset(t))

        self.showBoard()

    def b_click(self, b, x, y, t):

        if b["text"] == " " and self.clicked == True:
            b["text"] = "X"
            self.clicked = False
            self.count += 1
            self.board[x][y] = "X"
            self.ifwon(t)
            self.currplayer = Label(t, text="PLAYER 2(O)'s Move:", height=2,
                                    font=("COMIC SANS MS", 10, "bold"), bg="white")
            self.currplayer.grid(row=0, column=0)
        elif b["text"] == " " and self.clicked == False:
            b["text"] = "O"
            self.clicked = True
            self.count += 1
            self.board[x][y] = "O"
            self.ifwon(t)
            self.currplayer = Label(t, text="PLAYER 1(X)'s Move:", height=2,
                                    font=("COMIC SANS MS", 10, "bold"), bg="white")
            self.currplayer.grid(row=0, column=0)
        else:
            messagebox.showerror("Tic Tac Toe", "please select another box!")

    def ifwon(self, t):
        board = self.board
        if (board[0][0] == board[0][1] == board[0][2] == "X" or board[1][0] == board[1][1] == board[1][2] == "X" or board[2][0] == board[2][1] == board[2][2] == "X" or
            board[0][0] == board[1][0] == board[2][0] == "X" or board[0][1] == board[1][1] == board[2][1] == "X" or board[0][2] == board[1][2] == board[2][2] == "X" or
                board[0][0] == board[1][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X"):

            messagebox.showinfo("Victory", "Player 1(X) Wins!")
            self.currplayer = Label(t, text="PLAYER 1(X) won", height=2,
                                    font=("COMIC SANS MS", 10, "bold"), bg="white")
            self.currplayer.grid(row=0, column=0)
            self.disable_all_buttons()

        elif (board[0][0] == board[0][1] == board[0][2] == "O" or board[1][0] == board[1][1] == board[1][2] == "O" or board[2][0] == board[2][1] == board[2][2] == "O" or
              board[0][0] == board[1][0] == board[2][0] == "O" or board[0][1] == board[1][1] == board[2][1] == "O" or board[0][2] == board[1][2] == board[2][2] == "O" or
              board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O"):

            messagebox.showinfo("Victory", "Player 2(O) Wins!")
            self.currplayer = Label(t, text="PLAYER 2(O) won", height=2,
                                    font=("COMIC SANS MS", 10, "bold"), bg="white")
            self.currplayer.grid(row=0, column=0)
            self.disable_all_buttons()

        elif self.count == 9:
            messagebox.showinfo("Draw", "It's a Draw!")
            self.currplayer = Label(t, text="Draw", height=2,
                                    font=("COMIC SANS MS", 10, "bold"), bg="white")
            self.currplayer.grid(row=0, column=0)
            self.disable_all_buttons()

    def disable_all_buttons(self):
        self.b1.config(state=DISABLED)
        self.b2.config(state=DISABLED)
        self.b3.config(state=DISABLED)
        self.b4.config(state=DISABLED)
        self.b5.config(state=DISABLED)
        self.b6.config(state=DISABLED)
        self.b7.config(state=DISABLED)
        self.b8.config(state=DISABLED)
        self.b9.config(state=DISABLED)
