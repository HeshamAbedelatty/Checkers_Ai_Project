def minimax(board, capture ,player,depth, maximizing_player):
    if depth == 0 or is_game_over(board):
        return evaluate(board,capture,player), None

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        M = generate_moves(board,BLACK)
        N = generate_moves(board,BKING)
        if  N:
            for i in range (len(N)):
                M.append(N[i])
        for move in M:
            new_board = copy.deepcopy(board)
            make_move(new_board,move[0],move[1],move[2],move[3],move[4])
            eval, _ = minimax(new_board,move[5],move[0], depth - 1,False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        M = generate_moves(board,WHITE)
        N = generate_moves(board,WKING)
        if  N:
            for i in range (len(N)):
                M.append(N[i])
        for move in M:
            new_board = copy.deepcopy(board)
            make_move(new_board,move[0],move[1],move[2],move[3],move[4])
            eval, _ = minimax(new_board,move[5],move[0], depth - 1,  True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move
# alpha_beta algorithm with Alpha-Beta pruning
def alpha_beta(board,capture ,player,depth, alpha, beta, maximizing_player):
    if depth == 0 or is_game_over(board):
        return evaluate(board,capture,player), None

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        M = generate_moves(board,BLACK)
        N = generate_moves(board,BKING)
        if  N:
            for i in range (len(N)):
                M.append(N[i])
        for move in M:
            new_board = copy.deepcopy(board)
            make_move(new_board,move[0],move[1],move[2],move[3],move[4])
            eval, _ = alpha_beta(new_board,move[5],move[0], depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if alpha >= beta:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        M = generate_moves(board,WHITE)
        N = generate_moves(board,WKING)
        if  N:
            for i in range (len(N)):
                M.append(N[i])
        for move in M:
            new_board = copy.deepcopy(board)
            make_move(new_board,move[0],move[1],move[2],move[3],move[4])
            eval, _ = alpha_beta(new_board,move[5],move[0], depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if alpha >= beta:
                break
        return min_eval, best_move
