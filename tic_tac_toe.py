from enum import Enum
from typing import Optional
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

    def __str__(self):
        output = ""
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                output += f"{self._board[i][j]}"
            output += os.linesep
            if i < len(self._board) - 1:
                output += '-' * 9
                output += os.linesep

        return output

    def move(self, x: int, y: int, selection: TicTacToeSelection):
        if self._board[x][y] is TicTacToeSelection.EMPTY:
            self._board[x][y] = selection

    def validate_win(self) -> Optional[TicTacToeSelection]:
        for row in self._board:
            if row.count(row[0]) == len(row) and row[0] is not TicTacToeSelection.EMPTY:
                return row[0]

        for col in range(len(self._board[0])):
            col_values = [row[col] for row in self._board]
            if col_values.count(col_values[0]) == len(col_values) and col_values[0] is not TicTacToeSelection.EMPTY:
                return col_values[0]

        if (self._board[0][0] == self._board[1][1] == self._board[2][2] and
                self._board[0][0] is not TicTacToeSelection.EMPTY):
            return self._board[0][0]

        if (self._board[0][2] == self._board[1][1] == self._board[2][0] and
                self._board[0][2] is not TicTacToeSelection.EMPTY):
            return self._board[0][2]

        return None

    def validate_tie(self) -> Optional[bool]:
        winner = self.validate_win()

        for row in self._board:
            if TicTacToeSelection.EMPTY in row:
                return None

        if winner is None:
            return True

        return False


if __name__ == '__main__':
    pass
