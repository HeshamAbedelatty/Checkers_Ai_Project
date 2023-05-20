import copy
import math



# Constants
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
BLACK = 1
WHITE = 2
WKING = 3
BKING = 4
Capture = 0
# Board size
ROWS = 8
COLS = 8

# Initialize the board
board = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0]
]

# Function to print the board
def print_board(board):
    print("   A B C D E F G H")
    print("  ----------------")
    for i in range(8):
        print(i + 1, "|", end="  ")
        for j in range(8):
            piece = board[i][j]
            if piece == EMPTY:
                print(".", end="  ")
            elif piece == BLACK:
                print("B", end="  ")
            elif piece == WHITE:
                print("W", end="  ")
            elif piece == WKING:
                print("WK", end="  ")
            elif piece == BKING:
                print("BK", end="  ")    
        print()
    print()
