from Board.Board import Board

class AI:

    def __init__(self, circle, opponent_circle, depth):
        self.__circle = circle
        self.__depth = depth
        self.__opponent_circle = opponent_circle

    def get_circle(self):
        return self.__circle

    def __str__(self):
        return "The computer is playing with circles of this color: " + str(self.__circle)


    def validate_move(self, board, column):
        """
        Checks is a search_move is valid or not.
        :param board: the current board
        :param column: the current column
        :return: False or True depending on the situation.
        """
        row = 5
        while row > -1:
            if board.board[row][column] == '⬤':
                return True
            row -= 1
        return False

    def copy_board(self, board, column, character):
        """
        Makes a copy of the current board.
        :param board: the current board
        :param column: the certain column
        :param character: the certain character
        :return: the virtual board
        """
        simulated_board = Board()
        for i in range(6):
            for j in range(7):
                simulated_board.board[i][j] = board.board[i][j]
        simulated_board.move(column, character)
        return simulated_board

    def search_move(self, board):
        """
        Searches for the best search_move on a copy board.
        :param board: the certain board
        :return: the best search_move
        """
        moves_possible = {}
        for row in range(7):
            if self.validate_move(board, row):
                second_board = self.copy_board(board, row, self.__circle)
                moves_possible[row] = -self.find(self.__depth - 1, second_board, self.__opponent_circle)
        best_score = -99999999
        best_move = None
        moves = moves_possible.items()
        for move,score in moves:
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def find(self, depth_of_move, board, circle):
        """
        Finds the score of a search_move by recursively completing a virtual board until the depth parameter reaches 0
        :param depth_of_move: the given depth
        :param board: the current board
        :param circle: the given circle
        :return: the score of the move.  
        """
        move_allowed = []
        for i in range(7):
            if self.validate_move(board, i):
                second_board = self.copy_board(board, i, circle)
                move_allowed.append(second_board)
        if depth_of_move == 0 or len(move_allowed) == 0 or board.is_game_won():
            return self.value(board, circle)
        if circle == self.__circle:
            opponent_circle = self.__opponent_circle
        else:
            opponent_circle = self.__circle
        score = -99999999
        for i in move_allowed:
            score = max(score, -self.find(depth_of_move - 1, i, opponent_circle))
        return score

    def find_vertical_connection(self, row, column, board, length, circle):
        """
        Find if there exists a vertical connection within the board.
        :param row: the given row
        :param column: the given column
        :param board: the given board
        :param length: the given length
        :param circle: the given circle
        :return:  1 or 0 depending on the situation.
        """
        connection = 0
        if row + length - 1 < 6:
            for item in range(length):
                if board.board[row + item][column] == circle:
                    connection += 1
                else:
                    break
        if connection == length:
            return 1
        else:
            return 0

    def find_horizontal_connection(self, row, column, board, length, circle):
        """
        Finds if there exists a horizontal connection on a given board.
        :param row: the given row
        :param column: the given column
        :param board:  the given board
        :param length:  the given length
        :param circle: the given circle
        :return: 1 or 0 depending on the situation.
        """
        connection = 0
        if column + length - 1 < 7:
            for element in range(length):
                if circle == board.board[row][column + element]:
                    connection += 1
                else:
                    element = length + 1
        if connection == length:
            return 1
        else:
            return 0
    def find_diagonal_connection(self, row, column, board, length, circle):
        """
        Calculates the number of diagonal connection on a certain move.
        :param row:the given row
        :param column:the given column
        :param board:the given board
        :param length:the given length
        :param circle: the given circle
        :return: 1 or 0 depending on the situation.
        """
        total_connections = 0
        count_connection = 0
        if column + length - 1 < 7 and row + length - 1 < 6:
            for element in range(length):
                if circle == board.board[row + element][column + element]:
                    count_connection += 1
                else:
                    element = length + 1
        if count_connection == length:
            total_connections += 1
        count_connection = 0
        if column + length - 1 < 7 and row - length + 1 > -1:
            for element in range(length):
                if circle == board.board[row - element][column + element]:
                    count_connection += 1
                else:
                    element = length + 1
        if count_connection == length:
            total_connections += 1
        return total_connections


    def check_for_connection(self, board, circle, length):
        """
        Calculates the number of connections of certain length for a configuration of the board for a certain player
        :param board:the certain board
        :param circle: the certain circle
        :param length: the certain length
        :return:
        """
        connection_count = 0
        for row in range(6):
            for column in range(7):
                if board.board[row][column] == circle:
                    connection_count += self.find_vertical_connection(row, column, board, length, board.board[row][column])
                    connection_count += self.find_horizontal_connection(row, column, board, length, board.board[row][column])
                    connection_count += self.find_diagonal_connection(row, column, board, length, board.board[row][column])
        return connection_count

    def value(self, board, circle):
        """
        Calculates the number of connection each player using a heuristic.
        :param board:the certain board
        :param circle: the certain  circle
        :return: the connection
        """
        if circle == self.__circle:
            circle_opponent = self.__opponent_circle
        else:
            circle_opponent = self.__circle
        player_fourth_connection = self.check_for_connection(board, circle, 4)
        player_three_connection = self.check_for_connection(board, circle, 3)
        player_two_connection = self.check_for_connection(board, circle, 2)
        opponent_fourth_connection = self.check_for_connection(board, circle_opponent, 4)
        opponent_three_connection = self.check_for_connection(board, circle_opponent, 3)
        opponent_two_connection = self.check_for_connection(board, circle_opponent, 2)
        if opponent_fourth_connection > 0:
            return -100000
        else:
            return player_fourth_connection * 100000 + player_three_connection * 100 + player_two_connection - opponent_three_connection * 100 - opponent_two_connection