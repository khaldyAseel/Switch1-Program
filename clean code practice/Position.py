class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __add__(self, other):
        return Position(self.row + other.row, self.col + other.col)

    def __repr__(self):
        return f"Position({self.row}, {self.col})"
