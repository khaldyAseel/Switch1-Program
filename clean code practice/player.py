from Position import Position

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.position = None  # Position will be set during game setup

    def _update_score(self, points):
        """Update player's score."""
        self.score += points

    def set_position(self, position):
        """Set player's position on the board."""
        self.position = position

    def move(self, delta_row, delta_col):
        """Move the player to a new position."""
        if self.position:
            new_position = self.position + Position(delta_row, delta_col)
            self.position = new_position
