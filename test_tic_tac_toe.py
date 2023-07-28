import unittest
from tic_tac_toe import TicTacToeBoard
import os


class TicTacToeTest(unittest.TestCase):
    def test_initialization_of_empty_board(self):
        tic_tac_toe_board = TicTacToeBoard()
        actual = tic_tac_toe_board.print_board()
        expected = f"[ ][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}---------{os.linesep}[ ][ ][ ]{os.linesep}"

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
