class Square:
    EMPTY = "."
    COIN = "coin"
    BONUS = "bonus"
    WALL = "wall"

    def __init__(self, square_type=EMPTY):
        self.square_type = square_type
        self.occupied_by = None

    def __str__(self):
        """Return a string representation of the square."""
        if self.occupied_by:
            return self.occupied_by  # If the square is occupied, return the player name
        return self.square_type  # Otherwise, return the square type (coin, wall, etc.)
    
    def is_occupied(self):
        """Check if the square is occupied by a player."""
        return self.occupied_by is not None

    def occupy(self, player):
        """Mark the square as occupied by a player."""
        self.occupied_by = player

    def vacate(self):
        """Mark the square as no longer occupied."""
        self.occupied_by = None
