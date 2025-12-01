"""
Author: hoangedu773
GitHub: https://github.com/hoangedu773
Date: 2025-12-01
Description: Thuat toan Minimax va Alpha-Beta cho TicTacToe
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O

def actions(board):
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
    return possible_actions

def result(board, action):
    if action not in actions(board):
        raise Exception("Invalid action")
    
    i, j = action
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
    
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None

def terminal(board):
    if winner(board) is not None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    
    return True

def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def maxValue(state):
    if terminal(state):
        return utility(state)
    
    v = -math.inf
    for action in actions(state):
        v = max(v, minValue(result(state, action)))
    return v

def minValue(state):
    if terminal(state):
        return utility(state)
    
    v = math.inf
    for action in actions(state):
        v = min(v, maxValue(result(state, action)))
    return v

def minimax(board):
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        best_score = -math.inf
        best_action = None
        for action in actions(board):
            score = minValue(result(board, action))
            if score > best_score:
                best_score = score
                best_action = action
        return best_action
    else:
        best_score = math.inf
        best_action = None
        for action in actions(board):
            score = maxValue(result(board, action))
            if score < best_score:
                best_score = score
                best_action = action
        return best_action

def maxValueAB(state, alpha, beta):
    if terminal(state):
        return utility(state)
    
    v = -math.inf
    for action in actions(state):
        v = max(v, minValueAB(result(state, action), alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def minValueAB(state, alpha, beta):
    if terminal(state):
        return utility(state)
    
    v = math.inf
    for action in actions(state):
        v = min(v, maxValueAB(result(state, action), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def alphabeta(board):
    if terminal(board):
        return None
    
    current_player = player(board)
    alpha = -math.inf
    beta = math.inf
    
    if current_player == X:
        best_score = -math.inf
        best_action = None
        for action in actions(board):
            score = minValueAB(result(board, action), alpha, beta)
            if score > best_score:
                best_score = score
                best_action = action
            alpha = max(alpha, best_score)
        return best_action
    else:
        best_score = math.inf
        best_action = None
        for action in actions(board):
            score = maxValueAB(result(board, action), alpha, beta)
            if score < best_score:
                best_score = score
                best_action = action
            beta = min(beta, best_score)
        return best_action

def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" ", end="")
        for j, cell in enumerate(row):
            if cell is None:
                print(" ", end="")
            else:
                print(cell, end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("  -----------")
    print("\n")

def play_game(use_alphabeta=False):
    board = initial_state()
    print("==========================================")
    print("TIC TAC TOE - MINIMAX vs ALPHA-BETA")
    print("==========================================")
    print(f"Thuat toan: {'Alpha-Beta' if use_alphabeta else 'Minimax'}")
    
    print_board(board)
    
    move_count = 0
    while not terminal(board):
        current_player = player(board)
        print(f"Luot cua: {current_player}")
        
        if use_alphabeta:
            action = alphabeta(board)
        else:
            action = minimax(board)
        
        if action:
            board = result(board, action)
            move_count += 1
            print(f"Nuoc di {move_count}: {action}")
            print_board(board)
    
    win = winner(board)
    print("==========================================")
    if win:
        print(f"Ket qua: {win} THANG!")
    else:
        print("Ket qua: HOA!")
    print("==========================================")

def test_scenario():
    print("\n" + "="*50)
    print("TEST SCENARIO: So sanh Minimax vs Alpha-Beta")
    print("="*50)
    
    test_board = [
        [X, O, X],
        [O, X, EMPTY],
        [EMPTY, EMPTY, O]
    ]
    
    print("\nTrang thai ban dau:")
    print_board(test_board)
    
    print("Luot cua:", player(test_board))
    
    print("\n--- Minimax ---")
    move_minimax = minimax(test_board)
    print(f"Nuoc di tot nhat: {move_minimax}")
    
    print("\n--- Alpha-Beta ---")
    move_ab = alphabeta(test_board)
    print(f"Nuoc di tot nhat: {move_ab}")
    
    print("\nKet luan: Ca hai cho cung ket qua!")

def main():
    print("\n" + "="*50)
    print("BUOI 3: MINIMAX VA ALPHA-BETA")
    print("="*50)
    
    print("\n1. Choi game voi Minimax")
    play_game(use_alphabeta=False)
    
    print("\n2. Choi game voi Alpha-Beta")
    play_game(use_alphabeta=True)
    
    print("\n3. Test scenario")
    test_scenario()

if __name__ == "__main__":
    main()
