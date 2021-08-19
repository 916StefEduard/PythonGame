from Circle.Circle import Circle
from Board.Board import Board
from AI.AI import AI
from Player.Player import Player

class UI:

    def __init__(self,board):
        self.__board=board

    def __print_menu(self):
       print('\n')
       print("1. Start The Game")
       print("2. exit")


    def human_vs_computer(self):
        first_circle = Circle('red')
        second_circle = Circle('yellow')
        Human = Player(first_circle)
        Computer = AI(second_circle, first_circle, 4)
        board = Board()
        print("You have the following color:",Human)
        print(Computer)
        print(board)
        while(board.is_game_draw() == False):
            first_column = input("Player"+", choose your column: ")
            while (board.column_validator(first_column) == False):
                first_column = input("Please choose a number between 1 and 7: ")
            first_column = int(first_column)
            first_column -= 1
            while board.move(first_column, Human.get_circle()) == False:
                first_column = input("Please choose a column which is not full: ")
                while (board.column_validator(first_column) == False):
                    first_column = input("Please choose a number between 1 and 7: ")
                first_column = int(first_column)
                first_column -= 1
            print(board)
            if board.is_game_won() == True:
                print("Player" + " wins.")
                break
            second_column = int(Computer.search_move(board))
            print("The computer chose column: " + str(second_column + 1))
            board.move(second_column,Computer.get_circle())
            print(board)
            if board.is_game_won() == True:
                print("The computer wins.")
                break
        if board.is_game_draw() == True:
            print("Draw")

    def start(self):
        commands = {'1': self.human_vs_computer}
        while True:
            self.__print_menu()
            command = input("command: ")
            if command == '2':
                break
            commands[command]()


