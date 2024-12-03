from board import Board
from card import Card

class Game:
    def __init__(self, board_size):
        self.board = Board(board_size)
        self.turns = 0

    def play(self):
        pairs_found = 0

        while not self.board.all_cards_matched():
            self.board.display_board()
            
            try:
                index1 = int(input("Enter the index of the first card: "))
                index2 = int(input("Enter the index of the second card: "))
                
                if index1 == index2:
                    print("You must choose two different cards. Try again.")
                    continue
                
                self.board.cards[index1].flip()
                self.board.cards[index2].flip()

                self.board.display_board()

                if self.board.is_match(index1, index2):
                    print("Match found!")
                else:
                    print("No match. Try again.")
                    self.board.cards[index1].flip()
                    self.board.cards[index2].flip()

                self.turns += 1
            except (ValueError, IndexError):
                print("Invalid input. Please choose valid card indices.")

        print(f"Congratulations! You completed the game in {self.turns} turns.")

# Example usage
if __name__ == "__main__":
    board_size = 4  # Board size should be an even number
    game = Game(board_size)
    game.play()