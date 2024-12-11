from Matrix import Matrix
from square import Square
from player import Player
from Position import Position 
import random

LOW_COINS_THRESHOLD = 10
WINNING_SCORE = 100

class GoldRush(Matrix):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.players = {"player1": Player("player1"), "player2": Player("player2")}
        self.win = ""
        self.coins = 0

    def load_board(self):
        if self.rows == 0 and self.cols == 0:
            self.matrix = []
            return

        self.matrix = []
        elements = [Square.COIN, Square.EMPTY, Square.WALL]
        coins = 0

        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.cols):
                if i % 2 != 0:
                    rand_index = random.randint(0, 2)
                    rand_element = elements[rand_index]
                    square = Square(rand_element)
                    self.matrix[i].append(square)
                    if rand_element == Square.COIN:
                        coins += 1
                else:
                    wall_index = 2
                    wall = elements[wall_index]
                    square = Square(wall)
                    self.matrix[i].append(square)

            rand = random.randint(1, 2)
            for k in range(1, self.cols, rand):
                rand += 1
                rand_index = random.randint(0, 2)
                rand_element = elements[rand_index]
                self.matrix[i][k] = Square(rand_element)
                if rand_element == Square.COIN:
                    coins += 1

        # Place players in the starting positions
        self.matrix[0][0] = Square("player1")
        self.matrix[self.rows - 1][self.cols - 1] = Square("player2")
        self.coins = coins

        if coins < LOW_COINS_THRESHOLD:  # Threshold check
            return self.load_board()
        else:
            return self.matrix

    def _check_win(self, player):
        score = self.players[player].score
        if score >= WINNING_SCORE:
            self.win = player
            return True
        return False

    def _get_opponent(self, player):
        return "player2" if player == "player1" else "player1"

    def _perform_move(self, player, delta_row, delta_col):
        current_position = self.players[player].position
        if not current_position:
            return  # Player not found

        new_position = Position(current_position.row + delta_row, current_position.col + delta_col)

        if not (0 <= new_position.row < self.rows and 0 <= new_position.col < self.cols):
            return  # Out of bounds

        target_cell = self.matrix[new_position.row][new_position.col]
        opponent = self._get_opponent(player)

        if not target_cell.is_occupied() or target_cell.occupied_by != opponent:
            if target_cell.square_type == Square.COIN:
                self.players[player]._update_score(10)

            # Move player
            old_position = self.players[player].position
            self.matrix[old_position.row][old_position.col].vacate()
            self.matrix[new_position.row][new_position.col].occupy(player)

            self.players[player].set_position(new_position)

        return self._check_win(player)

    def _find_player_position(self, player):
        for r, row in enumerate(self.matrix):
            for c, square in enumerate(row):
                if square.is_occupied() and square.occupied_by == player:
                    return r, c
        return None, None
    
    def _move_player(self, player, direction):
        curr_row, curr_col = self._find_player_position(player)

        if curr_row is None or curr_col is None:
            return  # Player not found

        if direction == "down":
            return self.move_down(curr_row, curr_col, player)
        elif direction == "up":
            return self.move_up(curr_row, curr_col, player)
        elif direction == "right":
            return self.move_right(curr_row, curr_col, player)
        elif direction == "left":
            return self.move_left(curr_row, curr_col, player)

    def move_down(self, curr_row, curr_col, player):
        print("downnn")
        return self._perform_move(curr_row, curr_col, player, 1, 0)

    def move_up(self, curr_row, curr_col, player):
        return self._perform_move(curr_row, curr_col, player, -1, 0)

    def move_right(self, curr_row, curr_col, player):
        return self._perform_move(curr_row, curr_col, player, 0, 1)

    def move_left(self, curr_row, curr_col, player):
        return self._perform_move(curr_row, curr_col, player, 0, -1)

