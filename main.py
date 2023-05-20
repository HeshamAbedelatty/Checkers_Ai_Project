# Main game loop
def play_game():
    fun = 0
    lEasy = 4
    lMid = 6
    lHard = 8
    level = lEasy
    current_player = PLAYER_X
    while not is_game_over(board):
        print_board(board)
        if fun == 0:

            if current_player == PLAYER_X:
                print("Player Black's turn:")
                # _, move = alpha_beta(board,0,0, 4, float('-inf'), float('inf'), True)
                _, move = minimax(board, 0, 0, level, True)
            else:
                print("Player White's turn:")
                # _, move = alpha_beta(board,0,0,4, float('-inf'), float('inf'), False)
                _, move = minimax(board, 0, 0, level, False)
            if move:
                make_move(board, move[0], move[1], move[2], move[3], move[4])
            else:
                print("No valid moves.")
                break

            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

            print_board(board)
        else:

            if current_player == PLAYER_X:
                print("Player Black's turn:")
                _, move = alpha_beta(board, 0, 0, level, float('-inf'), float('inf'), True)
                # _, move = minimax(board,0,0, 4, True)
            else:
                print("Player White's turn:")
                _, move = alpha_beta(board, 0, 0, level, float('-inf'), float('inf'), False)
                # _, move = minimax(board,0,0,4, False)
            if move:
                make_move(board, move[0], move[1], move[2], move[3], move[4])
            else:
                print("No valid moves.")
                break

            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

            print_board(board)
    if is_game_over(board):
        score_x = evaluate(board, 0, BLACK)
        score_o = evaluate(board, 0, WHITE)
        score_w = evaluate(board, 0, WKING)
        score_b = evaluate(board, 0, BKING)
        if score_x > score_o or score_b > score_w:
            print("Player White wins!")
        elif score_x < score_o or score_b < score_w:
            print("Player Black wins!")
        else:
            print("It's a draw!")


# Start the game
play_game()