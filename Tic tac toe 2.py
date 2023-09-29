# Program for Tic Tac Toe
# Board Display
board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']


# Function to check if the board is full or not
def is_full(board):
    return '_' not in board


# Function to check if there is a winner or not
def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != '_':
            return board[i]
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != '_':
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] != '_':
        return board[0]
    if board[2] == board[4] == board[6] != '_':
        return board[2]
    # No winner
    return None


# Function to evaluate the score of the board
def evaluate(board):
    winner = check_winner(board)
    if winner == 'O':  # AI wins
        return 1
    elif winner == 'X':  # Human wins
        return -1
    else:  # Tie or no winner yet
        return 0


# Function to implement the Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    # Base case: terminal state or depth limit reached
    if is_full(board) or check_winner(board) or depth == 0:
        return evaluate(board)

    # Recursive case: exploring possible moves and choosing the best one
    if is_maximizing:  # AI's turn
        best_score = -float('inf')  # Initialize the best score to negative infinity
        for i in range(9):  # Loop through all the cells
            if board[i] == '_':  # If the cell is empty
                board[i] = 'O'  # Make the move
                score = minimax(board, depth - 1, alpha, beta, False)  # Recursively call minimax on the new board
                board[i] = '_'  # Undo the move
                best_score = max(best_score, score)  # Update the best score
                alpha = max(alpha, best_score)  # Update the alpha value
                if beta <= alpha:  # If beta cut-off occurs, stop exploring this branch
                    break
        return best_score  # Return the best score for this move

    else:  # Human's turn
        best_score = float('inf')  # Initialize the best score to positive infinity
        for i in range(9):  # Loop through all the cells
            if board[i] == '_':  # If the cell is empty
                board[i] = 'X'  # Make the move
                score = minimax(board, depth - 1, alpha, beta, True)  # Recursively call minimax on the new board
                board[i] = '_'  # Undo the move
                best_score = min(best_score, score)  # Update the best score
                beta = min(beta, best_score)  # Update the beta value
                if beta <= alpha:  # If alpha cut-off occurs, stop exploring this branch
                    break
        return best_score  # Return the best score for this move


# Function to find the best move for the AI player
def find_best_move(board):
    best_score = -float('inf')  # Initializing the best score to negative infinity
    best_move = None  # Initializing the best move to None

    for i in range(9):  # Loop through all the cells
        if board[i] == '_':  # If the cell is empty
            board[i] = 'O'  # Make the move
            score = minimax(board, 8, -float('inf'), float('inf'),
                            False)  # Call minimax on the new board with depth limit of 8 (can be changed)
            board[i] = '_'  # Undo the move

            if score > best_score:  # If this move has a better score than the current best score
                best_score = score  # Update the best score
                best_move = i  # Update the best move

    return best_move  # Return the best move


# Function to print the board in a nice format
def print_board(board):
    print()
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()


# Define a function to play the game
def play():
    global board  # Use the global board variable
    print("Welcome to Tic-Tac-Toe!")
    print("You are X and the AI is O")
    print("Enter a number from 1 to 9 to choose a cell")
    print("The cells are numbered from left to right, top to bottom")
    print_board(board)  # Print the initial board

    while True:  # Loop until the game is over
        # Human's turn
        move = input("Enter your move: ")  # Get the input from the user
        try:  # To convert the input to an integer
            move = int(move) - 1  # Subtract 1 to get the index of the cell
            if move < 0 or move > 8:  # If the move is out of range
                raise ValueError  # Raise an error
        except ValueError:  # If the input is not a valid integer
            print("Invalid input. Please enter a number from 1 to 9.")  # Print an error message
            continue  # Skip the rest of this iteration and go back to the loop

        if board[move] != '_':  # If the cell is not empty
            print("That cell is already taken. Please choose another one.")  # Print an error message
            continue  # Skip the rest of this iteration and go back to the loop

        board[move] = 'X'  # Make the move
        print_board(board)  # Print the updated board

        winner = check_winner(board)  # Check if there is a winner
        if winner == 'X':  # If the human player wins
            print("You win!")  # Print a congratulatory message
            break  # Break out of the loop and end the game
        elif winner == 'O':  # If the AI player wins
            print("You lose!")  # Print a commiserating message
            break  # Break out of the loop and end the game
        elif is_full(board):  # If the board is full and there is no winner
            print("It's a tie!")  # Print a neutral message
            break  # Break out of the loop and end the game

        # AI's turn
        print("AI's turn...")
        move = find_best_move(board)  # Find the best move for the AI player
        board[move] = 'O'  # Make the move
        print_board(board)  # Print the updated board

        winner = check_winner(board)  # Check if there is a winner
        if winner == 'X':  # If the human player wins
            print("You win!")  # Print a congratulatory message
            break  # Break out of the loop and end the game
        elif winner == 'O':  # If the AI player wins
            print("You lose!")  # Print a commiserating message
            break  # Break out of the loop and end the game
        elif is_full(board):  # If the board is full and there is no winner
            print("It's a tie!")  # Print a neutral message
            break  # Break out of the loop and end the game


# Calling the play function to start the game
play()
