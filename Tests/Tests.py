import unittest
from Player.Player import Player
from Board.Board import Board
from AI.AI import AI
from Circle.Circle import Circle

class Tests(unittest.TestCase):

    def test_board(self):
        first_circle = Circle('yellow')
        second_circle = Circle('magenta')
        board = Board()
        board.board[4][2] = second_circle
        board.board[2][2] = second_circle
        board.board[4][0] = first_circle
        board.board[0][2] = second_circle
        assert board.board[4][0] == first_circle
        assert board.is_game_won() == False
        assert board.is_game_draw() == False
        assert board.is_game_won() == False

    def test_player(self):
        first_circle = Circle('yellow')
        second_circle = Circle('blue')
        first_player = Player(first_circle)
        second_player = Player(second_circle)
        assert first_player.get_circle() == first_circle
        assert second_player.get_circle() == second_circle

    def test_computer(self):
        first_circle = Circle('yellow')
        second_circle = Circle('blue')
        first_player = Player(first_circle)
        second_circle = AI(second_circle,first_player.get_circle(), 2)
        board = Board()
        board.board[5][0] = first_circle
        board.board[2][2] = second_circle
        board.board[1][2] = first_circle
        board.board[0][2] = second_circle
        assert second_circle.get_circle() == second_circle.get_circle()
        assert second_circle.validate_move(board, 2) == True
        assert second_circle.validate_move(board, 1) == True
        B2 = second_circle.copy_board(board, 1, second_circle.get_circle())
        assert second_circle.find_vertical_connection(4, 2, board, 3, second_circle) == 0
        assert second_circle.find_vertical_connection(5, 2, board, 2, second_circle) == 0
        assert second_circle.find_diagonal_connection(4, 2, board, 2, second_circle) == 0
        assert second_circle.check_for_connection(board, first_circle, 2) == 0
        assert second_circle.search_move(board) == 0

if __name__ == '__main__':
    unittest.main()