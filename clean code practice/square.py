class Square:
    EMPTY = "."
    COIN = "coin"
    BONUS = "bonus"
    WALL = "wall"

    def __init__(self, square_type=EMPTY):
        self.square_type = square_type
        self.occupied_by = None

    def is_occupied(self):
        """Check if the square is occupied by a player."""
        return self.occupied_by is not None

    def occupy(self, player):
        """Mark the square as occupied by a player."""
        self.occupied_by = player

    def vacate(self):
        """Mark the square as no longer occupied."""
        self.occupied_by = None
