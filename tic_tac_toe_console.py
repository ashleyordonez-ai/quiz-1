# tic_tac_toe_console.py
# Console-based Tic-Tac-Toe Game

board = [" "] * 9
current_player = "X"
game_over = False

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner():
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    if " " not in board:
        return "Tie"
    return None

while not game_over:
    print_board()
    move = input(f"Player {current_player}, choose a position (1-9): ")
    
    if not move.isdigit() or int(move) < 1 or int(move) > 9:
        print("Invalid input. Choose a number from 1 to 9.")
        continue
    
    move = int(move) - 1
    
    if board[move] != " ":
        print("That spot is already taken. Try again.")
        continue
    
    board[move] = current_player
    winner = check_winner()
    
    if winner:
        print_board()
        if winner == "Tie":
            print("It's a tie!")
        else:
            print(f"Player {winner} wins!")
        game_over = True
    else:
        current_player = "O" if current_player == "O" else "O"
