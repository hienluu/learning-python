# https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/connect-four
# https://www.youtube.com/watch?v=9UI4ikKP3Ws

# Design a Connect Four game
# "Build the object-oriented design for a two-player Connect Four game. 
# Players take turns dropping discs into a 7-column, 6-row board. 
# The first to align four of their own discs vertically, horizontally, or diagonally wins."

# requirements -> entities -> class design -> implementation -> extensibility
# entities (state, behavior)
# implementation: seudo code or exact
# extensibility: how the desing could evolve w/ additiona capability

###### requirements ######
# questions to asks 3 categories: 
#     (main capabilities, error handling, scope boundary (in/out))

from enum import Enum
from typing import Optional

class DiscColor(Enum):
    RED = "red"
    BLUE = "blue"

class Player:
    def __init__(self, name: str, color: DiscColor):
        self.name = name
        self.color = color

    def __str__(self) -> str:
        return f"Player(name={self.name}, color={self.color})"

    def get_color(self) -> DiscColor:
        return self.color

    def get_name(self) -> str:
        return self.name

class Board:
    def __init__(self, no_rows: int, no_columns: int):
        self.no_rows = no_rows
        self.no_columns = no_columns
        self.board: list[list[DiscColor]] = [[None for _ in range(no_columns)] for _ in range(no_rows)]

    def __str__(self) -> str:
        return f"Board(no_rows={self.no_rows}, no_columns={self.no_columns})"
    
    # print the board in a grid format and in human readable format, like a grid of dots and Xs and Os
    # with cell borders
    def print_board(self) -> None:
        for row in range(self.no_rows):
            for col in range(self.no_columns):
                disc_color = self.board[row][col]
                if disc_color is None:
                    print(".", end=" ")
                elif disc_color == DiscColor.RED:
                    print("r", end=" ")
                elif disc_color == DiscColor.BLUE:
                    print("b", end=" ")
            print()
        print()
    
    def get_board(self) -> list[list[DiscColor]]:
        return self.board

    def get_no_rows(self) -> int:
        return self.no_rows

    def get_no_columns(self) -> int:
        return self.no_columns

    # return the row where the disc is placed, return -1
    def place_disc(self, column: int, color: DiscColor) -> int:
        ## core logic
        # find the first empty row in the column
        # place disc in the row
        # return the row
        # start from the last row and go up
        # range(start, stop, step)
        for row in range(self.no_rows - 1, -1, -1): # start from the last row and go up
            if self.board[row][column] is None: # if the row is empty
                self.board[row][column] = color # place the disc
                return row # return the row
        return -1 # if the column is full, return -1
  
    def _is_valid_position(self, row:int, column:int) -> bool:
        return row >= 0 and row < self.no_rows and column >= 0 and column < self.no_columns

    def checkWin(self, row:int, column:int, disc_color: DiscColor) -> bool:
        ## core logic
        # check for win in the row
        # check for win in the column
        # check for win in the diagonal
        # return true if win, false otherwise
        ## edge cases
        # invalid row or column
        # color doesn't match the color at the row and column

        # initialize the directions array to simplify the logic of checking for win in the row, column, and diagonal
        directions = [
            (0, 1), # horizontal
            (1, 0), # vertical
            (1, 1), # diagonal right up
            (-1, 1), # diagonal left down
        ]

        if not self._is_valid_position(row, column):
            return False

        if self.board[row][column] != disc_color:
            return False

        for dr, dc in directions:
            count = 1 # count the disc at the current position and we check above about same color already
            count += self._countDiscsInDirection(row, column, disc_color, dr, dc)
            # the second check is for the opposite direction
            count += self._countDiscsInDirection(row, column, disc_color, -dr, -dc)
            if count >= 4:
                return True
        return False

    def _countDiscsInDirection(self, row:int, column:int, color: DiscColor, dr:int, dc:int) -> int:
        ## core logic
        # check for win in the direction
        # return the count of the discs in the direction
   
        
        count = 0
        r = row + dr
        c = column + dc
        while self._is_valid_position(r, c) and self.board[r][c] == color:
            count += 1
            r += dr
            c += dc

        return count
    
    
    def can_place_disc(self, column: int) -> bool:
        for row in range(self.no_rows):
            if self.board[row][column] is None:
                return True
        return False

    # booard is full, when all the cells on the board are not None
    # if one of the cells is None, the board is not full, return false
    def is_full(self) -> bool:
        for row in range(self.no_rows):
            for col in range(self.no_columns):
                if self.board[row][col] is None:
                    return False
        return True


class GameState(Enum):
    IN_PROGRESS = "in_progress"
    WON = "won"
    DRAW = "draw"

class Game:
    def __init__(self,  player1: Player, player2: Player, board: Board):
        self.player1: Player = player1
        self.player2: Player = player2
        self.board: Board = board
        self.current_player: Optional[Player] = player1
        self.winner: Optional[Player] = None
        self.game_state: GameState = GameState.IN_PROGRESS

    def __str__(self) -> str:
        return f"Game(player1={self.player1}, player2={self.player2}, board={self.board})"

    def get_current_player(self) -> Player:
        return self.current_player

    def get_winner(self) -> Optional[Player]:
        return self.winner

    def get_game_state(self) -> GameState:
        return self.game_state
    
    def get_board(self) -> Board:
        return self.board
    
    # 
    def make_move(self, player: Player, column: int) -> None:
        ## core logic
        # place disk
        # check for win, if true, set game state to won and set the winner
        # if not win, check for draw, if true, set game state to draw
        # switch player turn

        ## edge cases
        # invalid column
        # wrong turn
        # game is already won or draw

        if self.game_state != GameState.IN_PROGRESS:
            raise ValueError("Game is not in progress")

        if player != self.current_player:
            raise ValueError("It's not the current player's turn")

        row = self.board.place_disc(column, player.get_color())
        if row == -1:
            raise ValueError("Column is full")

        if self.board.checkWin(row, column, player.get_color()):
            self.game_state = GameState.WON
            self.winner = player
            print(f"Player {player.get_name()} won the game!")
            return True
        
        if self.board.is_full():  # if the board is full, it's a draw
            self.game_state = GameState.DRAW
            print("The game is a draw!")
            return True
        
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        return False


def main():
    board = Board(6, 7)
    player1 = Player("Player 1", DiscColor.RED)
    player2 = Player("Player 2", DiscColor.BLUE)
    game = Game(player1, player2, board)
    game.make_move(player1, 0)
    game.make_move(player2, 1)
    game.make_move(player1, 0)
    game.make_move(player2, 1)
    game.make_move(player1, 0)
    game.make_move(player2, 1)
    game.make_move(player1, 0)

    game.make_move(player2, 3)

    board.print_board()

if __name__ == "__main__":
    main()