import unittest
from tic_tac_toe import TicTacToeBoard, TicTacToeGame
from tic_tac_toe import TicTacToeSelection
import os


class TicTacToeTest(unittest.TestCase):
    def test_initialization_of_empty_board(self):
        tic_tac_toe_board = TicTacToeBoard()
        actual = str(tic_tac_toe_board)
        expected = f"[ ][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}"

        self.assertEqual(actual, expected)

    def test_add_O_move_to_board(self):
        tic_tac_toe_board = TicTacToeBoard()
        tic_tac_toe_board.add_move(0, 0, TicTacToeSelection.O)
        expected = f"[O][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}"
        actual = str(tic_tac_toe_board)

        self.assertEqual(actual, expected)

    def test_add_X_move_to_board(self):
        tic_tac_toe_board = TicTacToeBoard()
        tic_tac_toe_board.add_move(0, 0, TicTacToeSelection.X)
        expected = f"[X][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}"
        actual = str(tic_tac_toe_board)

        self.assertEqual(actual, expected)

    def test_add_selection_to_cell_that_already_has_value(self):
        tic_tac_toe_board = TicTacToeBoard()
        tic_tac_toe_board.add_move(0, 0, TicTacToeSelection.X)
        tic_tac_toe_board.add_move(0, 0, TicTacToeSelection.O)
        expected = f"[X][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}"
        actual = str(tic_tac_toe_board)

        self.assertEqual(actual, expected)

    def test_X_wins_the_row(self):
        tic_tac_toe_board = TicTacToeBoard()
        tic_tac_toe_board.add_move(0, 0, TicTacToeSelection.X)
        tic_tac_toe_board.add_move(0, 1, TicTacToeSelection.X)
        tic_tac_toe_board.add_move(0, 2, TicTacToeSelection.X)
        actual = tic_tac_toe_board.validate_win()

        self.assertEqual(actual, TicTacToeSelection.X)

    def test_O_wins_the_column(self):
        tic_tac_toe_board = TicTacToeBoard()
        tic_tac_toe_board.add_move(0, 0, TicTacToeSelection.O)
        tic_tac_toe_board.add_move(1, 0, TicTacToeSelection.O)
        tic_tac_toe_board.add_move(2, 0, TicTacToeSelection.O)
        actual = tic_tac_toe_board.validate_win()

        self.assertEqual(actual, TicTacToeSelection.O)

    def test_X_wins_the_diagonal(self):
        tic_tac_toe_board = TicTacToeBoard()
        tic_tac_toe_board.add_move(0, 0, TicTacToeSelection.X)
        tic_tac_toe_board.add_move(1, 1, TicTacToeSelection.X)
        tic_tac_toe_board.add_move(2, 2, TicTacToeSelection.X)
        actual = tic_tac_toe_board.validate_win()

        self.assertEqual(actual, TicTacToeSelection.X)

    def test_tie_game(self):
        tic_tac_toe_board = TicTacToeBoard()
        tic_tac_toe_board.add_move(0, 0, TicTacToeSelection.X)
        tic_tac_toe_board.add_move(0, 1, TicTacToeSelection.O)
        tic_tac_toe_board.add_move(0, 2, TicTacToeSelection.X)
        tic_tac_toe_board.add_move(1, 0, TicTacToeSelection.X)
        tic_tac_toe_board.add_move(1, 1, TicTacToeSelection.X)
        tic_tac_toe_board.add_move(1, 2, TicTacToeSelection.O)
        tic_tac_toe_board.add_move(2, 0, TicTacToeSelection.O)
        tic_tac_toe_board.add_move(2, 1, TicTacToeSelection.X)
        tic_tac_toe_board.add_move(2, 2, TicTacToeSelection.O)
        actual = tic_tac_toe_board.validate_tie()

        self.assertTrue(actual)

    def test_tie_game_when_board_is_not_full(self):
        tic_tac_toe_board = TicTacToeBoard()
        tic_tac_toe_board.add_move(0, 0, TicTacToeSelection.X)
        tic_tac_toe_board.add_move(0, 1, TicTacToeSelection.O)
        tic_tac_toe_board.add_move(0, 2, TicTacToeSelection.X)
        tic_tac_toe_board.add_move(1, 0, TicTacToeSelection.X)
        tic_tac_toe_board.add_move(1, 2, TicTacToeSelection.O)
        tic_tac_toe_board.add_move(2, 0, TicTacToeSelection.O)
        tic_tac_toe_board.add_move(2, 1, TicTacToeSelection.X)
        tic_tac_toe_board.add_move(2, 2, TicTacToeSelection.O)
        actual = tic_tac_toe_board.validate_tie()

        self.assertIsNone(actual)

    def test_adding_x_using_board_position(self):
        tic_tac_toe_game = TicTacToeGame()
        tic_tac_toe_game.make_move("ONE", TicTacToeSelection.X)
        actual = tic_tac_toe_game.get_current_board_state()
        expected = f"[X][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}"

        self.assertEqual(actual, expected)

    def test_adding_x_using_board_invalid_position(self):
        tic_tac_toe_game = TicTacToeGame()
        tic_tac_toe_game.make_move("FOO", TicTacToeSelection.X)
        actual = tic_tac_toe_game.get_current_board_state()
        expected = f"[ ][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}"

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
