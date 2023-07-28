import unittest
from tic_tac_toe import TicTacToeBoard
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
        tic_tac_toe_board.move(0, 0, TicTacToeSelection.O)
        expected = f"[O][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}"
        actual = str(tic_tac_toe_board)

        self.assertEqual(actual, expected)

    def test_add_X_move_to_board(self):
        tic_tac_toe_board = TicTacToeBoard()
        tic_tac_toe_board.move(0, 0, TicTacToeSelection.X)
        expected = f"[X][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}"
        actual = str(tic_tac_toe_board)

        self.assertEqual(actual, expected)

    def test_add_selection_to_cell_that_already_has_value(self):
        tic_tac_toe_board = TicTacToeBoard()
        tic_tac_toe_board.move(0, 0, TicTacToeSelection.X)
        tic_tac_toe_board.move(0, 0, TicTacToeSelection.O)
        expected = f"[X][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}"
        actual = str(tic_tac_toe_board)

        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
