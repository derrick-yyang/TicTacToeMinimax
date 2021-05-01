from game import game
from tkinter import *

def main():
    t = Tk()
    t.title('Tic-Tac-Toe')
    t.configure(bg='white')
    Game = game(t)
    Game.showBoard()
    t.mainloop()
    
if __name__ == "__main__":
    main()