from Matrix import Matrix
import random

class GoldRush(Matrix):

    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.s1 = 0
        self.s2 = 0
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
                    rand_index = random.randint(0, 2)
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
                rand_index = random.randint(0, 2)
                rand_element = elements[rand_index]
                self.matrix[i][k] = rand_element
                if rand_element == self.COIN:
                    coins += 1

        self.matrix[0][0] = "player1"
        self.matrix[self.rows - 1][self.cols - 1] = "player2"
        self.coins = coins

        if coins < LOW_COINS_THRESHOLD:  # Threshold check
            return self.load_board()
        else:
            return self.matrix

    def _check_win(self, player):
        player_num = player[-1]
        score = getattr(self, f"s{player_num}")
        if score >= WINNING_SCORE:
            self.win = player
            return True
        return False

    def _get_opponent(self, player):
        return "player2" if player == "player1" else "player1"

    def _perform_move(self, curr_row, curr_col, player, delta_row, delta_col):
        new_row, new_col = curr_row + delta_row, curr_col + delta_col

        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return  # Out of bounds

        target_cell = self.get(new_row, new_col)
        opponent = self._get_opponent(player)
        print (target_cell)

        if target_cell not in [self.WALL, opponent]:
            if target_cell == self.COIN:
                self._update_score(player, 10)

            self.alter(curr_row, curr_col, self.EMPTY) 
            self.alter(new_row, new_col, player)  # Move player

        return self._check_win(player)

    # def move_down(self, curr_row, curr_col, player):
    #     print("downnn")
    #     return self._perform_move(curr_row, curr_col, player, 1, 0)

    # def move_up(self, curr_row, curr_col, player):
    #     return self._perform_move(curr_row, curr_col, player, -1, 0)

    # def move_right(self, curr_row, curr_col, player):
    #     return self._perform_move(curr_row, curr_col, player, 0, 1)

    # def move_left(self, curr_row, curr_col, player):
    #     return self._perform_move(curr_row, curr_col, player, 0, -1)

    # def _find_player_position(self, player):
    #     for r, row in enumerate(self.matrix):
    #         for c, value in enumerate(row):
    #             if value == player:
    #                 return r, c
    #     return None, None

    # def _update_score(self, player, points):
    #     player_num = player[-1]
    #     score_attr = f"s{player_num}"
    #     setattr(self, score_attr, getattr(self, score_attr) + points)

    # def _move_player(self, player, direction):
    #     curr_row, curr_col = self._find_player_position(player)

    #     if curr_row is None or curr_col is None:
    #         return  # Player not found

    #     if direction == "down":
    #         return self.move_down(curr_row, curr_col, player)
    #     elif direction == "up":
    #         return self.move_up(curr_row, curr_col, player)
    #     elif direction == "right":
    #         return self.move_right(curr_row, curr_col, player)
    #     elif direction == "left":
    #         return self.move_left(curr_row, curr_col, player)
