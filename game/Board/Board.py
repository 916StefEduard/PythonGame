
class Board:

    def __init__(self):

        self.board = [['⬤' for x in range(7)] for y in range(6)]


    def is_game_won(self):
        """
        checks if the game was won be someone or the computer
        Returns True if the game was won, False otherwise
        """
        for row in range(6):
            for column in range(4):
                if self.board[row][column] != '⬤':
                    if self.board[row][column] == self.board[row][column + 1] == self.board[row][column + 2]==self.board[row][column] == self.board[row][column + 3]:
                                return True

        for row in range(7):
            for column in range(3):
                if self.board[column][row] != '⬤':
                    if self.board[column][row] == self.board[column + 1][row] == self.board[column + 2][row] == self.board[column + 3][row]:
                                return True

        for row in range(3):
            for column in range(4):
                if self.board[row][column] != '⬤':
                    if self.board[row][column] == self.board[row + 1][column + 1] == self.board[row + 2][column + 2] == self.board[row + 3][column + 3]:
                                return True

        for row in range(3):
            column = 6
            while column > 2:
                if self.board[row][column] != '⬤':
                    if self.board[row][column] == self.board[row + 1][column - 1]== self.board[row + 2][column - 2]== self.board[row + 3][column - 3]:
                                return True
                column -= 1

        return False

    def is_game_draw(self):
        """
        checks if the game is a draw
        Returns True if the game is a draw and False otherwise
        """
        for i in range(6):
            for j in range(7):
                if self.board[i][j] == '⬤':
                    return False

        return True

    def move(self, column,circle):
        """
        function that actively makes a search_move on the board
        :param circle: the circle of the player
        :param column: the column of the board
        :return: nothing
        """
        row = 5
        while row > -1:
            if self.board[row][column] == '⬤':
                self.board[row][column] =circle
                return True
            row -= 1
        return False

    def get_move(self, row, column):
        """
        Returns the move of a certain collumn and row.
        :param row: the row parameter
        :param column:the column parameter
        :return:
        """
        return self.board[row][column]

    @staticmethod
    def command_validator(command):
        """
        The function that validates the input entered in the game.
        :param command: the certain commmand
        :return: False or true depending on the result.
        """
        commands = ['1', '2', '3']
        if command in commands:
            return True
        else:
            return False

    @staticmethod
    def column_validator(column):
        """
        The function that validates the column entered into the game.
        :param column: the certain column
        :return:  False or true depending on the result.
        """
        if int(column) > 0 and int(column) < 8:
                return True
        return False

    def __str__(self):
        """
        Returns the configuration of the board.
        """
        board = '------------------\n'
        for i in range(6):
            for j in range(7):
                board += '|'
                board += str(self.board[i][j])
            board += '|\n'
            board += '------------------\n'
        return board