# Tic Tac Toe Game

def print_board(board):
    """
    Function to print the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """
    Function to check if a player has won.
    """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_full(board):
    """
    Function to check if the board is full.
    """
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """
    Main function to play Tic Tac Toe.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")
        
        # Get row and column input
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
        
        # Check if the spot is empty
        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("Spot already taken! Try again.")
            continue
        
        # Check for winner
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        # Check for draw
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        turn += 1

# Run the game
tic_tac_toe()
