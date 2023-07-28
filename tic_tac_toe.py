from enum import Enum
import os

class TicTacToeSelection(Enum):
    EMPTY = "[ ]"
    X = "[X]"
    O = "[O]"

    def __str__(self):
        return self.value


class TicTacToeBoard:
    def __init__(self):
        self._board = [[TicTacToeSelection.EMPTY for _ in range(3)] for _ in range(3)]

    # todo: rename this function
    def print_board(self):
        output = ""
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                output += f"{self._board[i][j]}"
            output += os.linesep
            if i < len(self._board) - 1:
                output += '-' * 9
                output += os.linesep

        return output


if __name__ == '__main__':
    pass
