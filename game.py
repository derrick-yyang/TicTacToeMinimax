from tkinter import *
from tkinter import messagebox
import random
import math

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
        self.available_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.winner = None

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
        self.winner = None
        self.available_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        #self.make_move(t)
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
            #print(self.available_moves)
            self.available_moves.remove(x * 3 + y)
            #print(self.available_moves)
            self.make_move(t)
        elif b["text"] == " " and self.clicked == False:
            b["text"] = "O"
            self.clicked = True
            self.count += 1
            self.board[x][y] = "O"
            self.ifwon(t)
            self.currplayer = Label(t, text="PLAYER 1(X)'s Move:", height=2,
                                    font=("COMIC SANS MS", 10, "bold"), bg="white")
            self.currplayer.grid(row=0, column=0)
            self.available_moves.remove(x * 3 + y)
            #self.make_move(t)

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
            self.winner = 'X'
            self.disable_all_buttons()

        elif (board[0][0] == board[0][1] == board[0][2] == "O" or board[1][0] == board[1][1] == board[1][2] == "O" or board[2][0] == board[2][1] == board[2][2] == "O" or
              board[0][0] == board[1][0] == board[2][0] == "O" or board[0][1] == board[1][1] == board[2][1] == "O" or board[0][2] == board[1][2] == board[2][2] == "O" or
              board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O"):

            messagebox.showinfo("Victory", "Player 2(O) Wins!")
            self.currplayer = Label(t, text="PLAYER 2(O) won", height=2,
                                    font=("COMIC SANS MS", 10, "bold"), bg="white")
            self.currplayer.grid(row=0, column=0)
            self.winner = 'O'
            self.disable_all_buttons()

        elif self.count == 9:
            messagebox.showinfo("Draw", "It's a Draw!")
            self.currplayer = Label(t, text="Draw", height=2,
                                    font=("COMIC SANS MS", 10, "bold"), bg="white")
            self.currplayer.grid(row=0, column=0)
            self.disable_all_buttons()

    def minimaxIfWin(self):
        board = self.board
        if (board[0][0] == board[0][1] == board[0][2] == "X" or board[1][0] == board[1][1] == board[1][2] == "X" or board[2][0] == board[2][1] == board[2][2] == "X" or
            board[0][0] == board[1][0] == board[2][0] == "X" or board[0][1] == board[1][1] == board[2][1] == "X" or board[0][2] == board[1][2] == board[2][2] == "X" or
                board[0][0] == board[1][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X"):

            self.winner = 'X'

        elif (board[0][0] == board[0][1] == board[0][2] == "O" or board[1][0] == board[1][1] == board[1][2] == "O" or board[2][0] == board[2][1] == board[2][2] == "O" or
              board[0][0] == board[1][0] == board[2][0] == "O" or board[0][1] == board[1][1] == board[2][1] == "O" or board[0][2] == board[1][2] == board[2][2] == "O" or
              board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O"):

            self.winner = 'O'

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
        
    def get_available_moves_num(self):
        count = 0
        for x in self.board:
            for y in x:
                if y == " ":
                    count += 1
        return count

    # Minimax AI
    def get_move(self):

        if len(self.available_moves) == 9:
            square = random.randint(1, 8)
        else:
            d = self.minimax('O')
            square = d['position']
            print(d)
        return square

    def minimax(self, player):
        max_player = 'O'
        other_player = 'O' if player == 'X' else 'X'
        #print(self.available_moves)
        # base case
        if self.winner == other_player:
            return {'position': None,
                    'score': 1 * (self.get_available_moves_num() + 1) if other_player == max_player else -1 * (
                        self.get_available_moves_num() + 1)
                    }
        elif not self.get_available_moves_num(): #draw
            return {'position': None,
                    'score': 0
                    }
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        old_avail_moves = self.available_moves.copy()
        for possible_move in old_avail_moves:
            # make the move on the game state (board array)
            x = int(possible_move / 3)
            y = possible_move - x * 3
            #print(x)
            #print(y)
            self.board[x][y] = player
            self.available_moves.remove(possible_move)
            self.minimaxIfWin()
            new_score = self.minimax(other_player)

            # undo the move
            self.board[x][y] = ' '
            self.winner = None
            self.available_moves = old_avail_moves.copy()
            new_score['position'] = possible_move
           
            # replace scores if needed
            if player == max_player:
                if new_score['score'] > best['score']:
                    best = new_score
            else:
                if new_score['score'] < best['score']:
                    best = new_score


        return best

    def make_move(self, t):
        move = self.get_move()
        print(move)
        x = int(move / 3)
        y = move - x * 3
        if move == 0:
            self.b_click(self.b1, x, y, t)
        elif move == 1:
            self.b_click(self.b2, x, y, t)
        elif move == 2:
            self.b_click(self.b3, x, y, t)
        elif move == 3:
            self.b_click(self.b4, x, y, t)
        elif move == 4:
            self.b_click(self.b5, x, y, t)
        elif move == 5:
            self.b_click(self.b6, x, y, t)
        elif move == 6:
            self.b_click(self.b7, x, y, t)
        elif move == 7:
            self.b_click(self.b8, x, y, t)
        elif move == 8:
            self.b_click(self.b9, x, y, t)