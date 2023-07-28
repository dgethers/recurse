from collections import namedtuple
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
        self._grid = [[TicTacToeSelection.EMPTY for _ in range(3)] for _ in range(3)]

    def __str__(self):
        output = ""
        for i in range(len(self._grid)):
            for j in range(len(self._grid[i])):
                output += f"{self._grid[i][j]}"
            output += os.linesep
            if i < len(self._grid) - 1:
                output += '-' * 9
                output += os.linesep

        return output

    def add_move(self, x: int, y: int, selection: TicTacToeSelection):
        if self._grid[x][y] is TicTacToeSelection.EMPTY:
            self._grid[x][y] = selection

    def validate_win(self) -> Optional[TicTacToeSelection]:
        for row in self._grid:
            if row.count(row[0]) == len(row) and row[0] is not TicTacToeSelection.EMPTY:
                return row[0]

        for col in range(len(self._grid[0])):
            col_values = [row[col] for row in self._grid]
            if col_values.count(col_values[0]) == len(col_values) and col_values[0] is not TicTacToeSelection.EMPTY:
                return col_values[0]

        if (self._grid[0][0] == self._grid[1][1] == self._grid[2][2] and
                self._grid[0][0] is not TicTacToeSelection.EMPTY):
            return self._grid[0][0]

        if (self._grid[0][2] == self._grid[1][1] == self._grid[2][0] and
                self._grid[0][2] is not TicTacToeSelection.EMPTY):
            return self._grid[0][2]

        return None

    def validate_tie(self) -> Optional[bool]:
        winner = self.validate_win()

        for row in self._grid:
            if TicTacToeSelection.EMPTY in row:
                return None

        if winner is None:
            return True

        return False


Cell = namedtuple('Cell', ['x', 'y'])


class TicTacToeGame:
    def __init__(self):
        self._board = TicTacToeBoard()
        self._positions = {"ONE": Cell(0, 0),
                           "TWO": Cell(0, 1),
                           "THREE": Cell(0, 2),
                           "FOUR": Cell(1, 0),
                           "FIVE": Cell(1, 1),
                           "SIX": Cell(1, 2),
                           "SEVEN": Cell(2, 0),
                           "EIGHT": Cell(2, 1),
                           "NINE": Cell(2, 2)}

    def make_move(self, move: str, selection: TicTacToeSelection):
        cell = self._positions.get(move)
        if cell:
            self._board.add_move(cell.x, cell.y, selection)

    def get_current_board_state(self) -> str:
        return str(self._board)


if __name__ == '__main__':
    pass
