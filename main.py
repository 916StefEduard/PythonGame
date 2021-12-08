from Board.Board import  Board
from UI.UI import UI
from GUI.GUI import GUI

if __name__ == '__main__':
    board=Board()
    print("\n")
    print("1.UI")
    print("2.GUI\n")
    command=int(input(">>>"))
    if command==1:
        Game = UI(board)
        Game.start()
    else:
        Game=GUI()
        Game.create_gui()
