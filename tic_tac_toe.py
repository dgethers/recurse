from collections import namedtuple
from enum import Enum
from typing import Optional, Dict
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
        self._valid_positions = self._positions.keys()

    def make_move(self, move: str, selection: TicTacToeSelection):
        cell = self._positions.get(move)
        if cell:
            self._board.add_move(cell.x, cell.y, selection)

    def get_current_board_state(self) -> str:
        return str(self._board)

    def check_for_winner(self) -> Optional[TicTacToeSelection]:
        return self._board.validate_win()

    def check_for_tie(self) -> Optional[bool]:
        return self._board.validate_tie()

    def is_valid_position(self, move: str) -> bool:
        return move.upper() in self._valid_positions


if __name__ == '__main__':
    print("The First Player's name")
    player_first = input("Please mention your name: ")
    print("\n")

    print("The Second Player's name")
    player_second = input("Please mention your name:  ")
    print("\n")

    current_player = player_first
    tic_tac_toe_game = TicTacToeGame()
    players = {player_first: TicTacToeSelection.X, player_second: TicTacToeSelection.O}
    turn_count = 1

    while True:
        try:
            print("TicTacToe game where each player will place a X or O on a 3 x 3 grid")
            print("Use the number from one to nine to represent where on the grid you would like to put your selection")
            print("You must spell the numbers, 1 is one and so on and so forth. Case does not matter")
            print("Adding a selection to a square with a value already will be ignored")
            print("The player ", current_player, " turn. Now you need to choose your block : ")
            print(tic_tac_toe_game.get_current_board_state())

            chance = input().upper()
            if tic_tac_toe_game.is_valid_position(chance) is False:
                print("This is an Invalid Input!!! Please try again!")
                continue

            tic_tac_toe_game.make_move(chance, players[current_player])

            winner = tic_tac_toe_game.check_for_winner()
            if winner:
                print("The winner is: ", current_player)
                break

            turn_count += 1

            if current_player is player_first:
                current_player = player_second
            else:
                current_player = player_first

            if turn_count > 9:
                tie = tic_tac_toe_game.check_for_tie()
                if tie:
                    print('Tie game detected')

        except ValueError:
            print("This is an Invalid Input!!! Please try again!")
            continue
