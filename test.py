def evaluate(board,capture, player):
    score = 0
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == player :
                score += 1   
            elif board[row][col] != EMPTY:    
                score -= 1
            if player == BKING:
                score += 10         
            if player == WKING:
                score += -5        
            if capture == 5:
                score += 20
            if capture == 6:
                score += 50 
            if capture == 7:
                score += -5         
    return score
def is_game_over(board):
    # Check if a player has no more pieces
    white_pieces = 0
    black_pieces = 0

    for row in board:
        for piece in row:
            if piece == WHITE or piece == WKING:
                white_pieces += 1
            elif piece == BLACK or piece == BKING :
                black_pieces += 1

    if white_pieces == 0 or black_pieces == 0:
        return True

    return False