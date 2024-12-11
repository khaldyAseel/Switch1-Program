from Matrix import Matrix
import random

LOW_COINS_THRESHOLD = 10
WINNING_SCORE = 100

class GoldRush(Matrix):
    COIN = "coin"
    EMPTY = "."
    WALL = "wall"

    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.score1 = 0
        self.score2 = 0
        self.win = ""
        self.coins = 0

    def load_board(self):
        if self.rows == 0 and self.cols == 0:
            self.matrix = []
            return

        self.matrix = []
        elements = [self.COIN, self.EMPTY, self.WALL]
        coins = 0

        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.cols):
                if i % 2 != 0:
                    rand_index = random.randint(0, 1)
                    rand_element = elements[rand_index]
                    self.matrix[i].append(rand_element)
                    if rand_element == self.COIN:
                        coins += 1
                else:
                    wall_index = 2
                    wall = elements[wall_index]
                    self.matrix[i].append(wall)

            rand = random.randint(1, 2)
            for k in range(1, self.cols, rand):
                rand += 1
                rand_index = random.randint(0, 1)
                rand_element = elements[rand_index]
                self.matrix[i][k] = rand_element
                if rand_element == self.COIN:
                    coins += 1

        self.matrix[0][0] = "player1"
        self.matrix[self.rows - 1][self.cols - 1] = "player2"
        self.coins = coins

        if coins < LOW_COINS_THRESHOLD:  # threshold
            return self.load_board()
        else:
            return self.matrix

    def _check_win(self, player):
        player_num = player[-1]
        score = getattr(self, f"score{player_num}")
        if score == WINNING_SCORE:
            self.win = player
            return self.win

    def _get_opponent(self, player):
        if player == "player1":
            return "player2"
        elif player == "player2":
            return "player1"

    def _perform_move(self, curr_row, curr_col, player, delta_row, delta_col):
        other_player = self._get_opponent(player)
        new_row, new_col = curr_row + delta_row, curr_col + delta_col

        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return

        if self.matrix[new_row][new_col] not in [self.WALL, other_player]:
            if self.matrix[new_row][new_col] == self.COIN:
                self._update_score(player)

            self.matrix[curr_row][curr_col] = self.EMPTY
            self.matrix[new_row][new_col] = player

        return self._check_win(player)

    def move_down(self, curr_row, curr_col, player):
        return self._perform_move(curr_row, curr_col, player, 1, 0)

    def move_up(self, curr_row, curr_col, player):
        return self._perform_move(curr_row, curr_col, player, -1, 0)

    def move_right(self, curr_row, curr_col, player):
        return self._perform_move(curr_row, curr_col, player, 0, 1)

    def move_left(self, curr_row, curr_col, player):
        return self._perform_move(curr_row, curr_col, player, 0, -1)

    def _move_player(self, player, direction):
        curr_row, curr_col = None, None

        for i, row in enumerate(self.matrix):
            for j, value in enumerate(row):
                if value == player:
                    curr_row, curr_col = i, j
                    break
            if curr_row is not None:
                break

        if direction == "down":
            self.move_down(curr_row, curr_col, player)
        elif direction == "up":
            self.move_up(curr_row, curr_col, player)
        elif direction == "right":
            self.move_right(curr_row, curr_col, player)
        elif direction == "left":
            self.move_left(curr_row, curr_col, player)

    def _update_score(self, player):
        player_num = player[-1]
        score_attr = f"score{player_num}"
        setattr(self, score_attr, getattr(self, score_attr) + 10)
        print(getattr(self, score_attr))
