
class player():

    def __init__(self):
        super().__init__()
        self.name = " "
        self.score = 0


    def _update_score(self, player, points):
        score_attr = f"s{score}"
        setattr(self, score_attr, getattr(self, score_attr) + points)

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

    def _find_player_position(self, player):
        for r, row in enumerate(self.matrix):
            for c, value in enumerate(row):
                if value == player:
                    return r, c
        return None, None

