import random
import time

rows = 8
cols = 8

# Create the board with placeholders for empty spaces and initial positions for pieces
board = [['[ ]' for _ in range(cols)] for _ in range(rows)]

# Define initial positions of pieces
initial_positions = {
    (0, 1): '@', (0, 3): '@', (0, 5): '@', (0, 7): '@',
    (1, 0): '@', (1, 2): '@', (1, 4): '@', (1, 6): '@',
    (2, 1): '@', (2, 3): '@', (2, 5): '@', (2, 7): '@',
    (5, 0): '#', (5, 2): '#', (5, 4): '#', (5, 6): '#',
    (6, 1): '#', (6, 3): '#', (6, 5): '#', (6, 7): '#',
    (7, 0): '#', (7, 2): '#', (7, 4): '#', (7, 6): '#'
}

# Place pieces on the board
for (row, col), piece in initial_positions.items():
    board[row][col] = '[{}]'.format(piece)

# Define column labels
column_labels = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Define players
HUMAN = '#'  # Human player uses '#' pieces
AI = '@'     # AI uses '@' pieces
current_player = HUMAN  # Human goes first

# AI types
ai_types = {
    "BasicBit": "Plays randomly with some capture prioritization",
    "Terminator": "Prioritizes capturing your pieces, even at the risk of losing its own",
    "Fortress": "Focuses on keeping its pieces safe, avoids risky moves",
    "Commander": "Tries to control the center of the board",
    "ForeSight": "Calculates multiple moves ahead and adapts to your playing style",
    "Chameleon": "Uses a mix of defensive and aggressive strategies with random surprises"
}

selected_ai = "Default"

# Function to print the board with coordinates
def print_board():
    print("\n   " + "  ".join(column_labels))
    for i, row in enumerate(board):
        print(str(i+1) + " " + "".join(row))
    print(f"\nCurrent player: {'Human' if current_player == HUMAN else f'AI ({selected_ai})'}")

# Function to reset the board
def reset_board():
    global board, current_player
    board = [['[ ]' for _ in range(cols)] for _ in range(rows)]
    for (row, col), piece in initial_positions.items():
        board[row][col] = '[{}]'.format(piece)
    current_player = HUMAN

# Function to check if coordinates are within the board
def is_valid_position(row, col):
    return 0 <= row < rows and 0 <= col < cols

# Function to check if a move is valid
def is_valid_move(from_row, from_col, to_row, to_col, player):
    # Check if destination is empty
    if board[to_row][to_col] != '[ ]':
        return False, None
    
    # Get the piece at the starting position
    piece = board[from_row][from_col].strip('[]')
    
    # Check if the piece belongs to the current player
    if piece != player:
        return False, None
    
    # Check if it's a valid move (diagonally forward for regular pieces)
    row_diff = to_row - from_row
    col_diff = to_col - from_col
    
    # For HUMAN pieces (#), they move up (negative row diff)
    # For AI pieces (@), they move down (positive row diff)
    direction = -1 if player == HUMAN else 1
    
    # Regular move (one step diagonally)
    if abs(col_diff) == 1 and row_diff == direction:
        return True, None
    
    # Capture move (two steps diagonally, jumping over opponent's piece)
    elif abs(col_diff) == 2 and row_diff == 2 * direction:
        # Check if there's an opponent's piece to capture
        captured_row = from_row + direction
        captured_col = from_col + (1 if col_diff > 0 else -1)
        
        if is_valid_position(captured_row, captured_col):
            captured_piece = board[captured_row][captured_col].strip('[]')
            if captured_piece == (AI if player == HUMAN else HUMAN):
                return True, (captured_row, captured_col)
    
    return False, None

# Function to move a piece on the board
def move_piece(from_row, from_col, to_row, to_col):
    global current_player
    
    # Check if the move is valid
    valid, captured = is_valid_move(from_row, from_col, to_row, to_col, current_player)
    
    if not valid:
        print("Invalid move.")
        return False
    
    # Move the piece
    piece = board[from_row][from_col]
    board[to_row][to_col] = piece
    board[from_row][from_col] = '[ ]'
    
    # If it's a capture move, remove the captured piece
    if captured:
        board[captured[0]][captured[1]] = '[ ]'
        print(f"Captured opponent's piece at {column_labels[captured[1]]}{captured[0]+1}!")
    
    # Switch player
    current_player = AI if current_player == HUMAN else HUMAN
    return True

# Function to get all valid moves for a player
def get_valid_moves(player):
    valid_moves = []
    
    for row in range(rows):
        for col in range(cols):
            if board[row][col].strip('[]') == player:
                # Check regular moves
                direction = -1 if player == HUMAN else 1
                
                # Check diagonally forward left
                to_row, to_col = row + direction, col - 1
                if is_valid_position(to_row, to_col):
                    valid, captured = is_valid_move(row, col, to_row, to_col, player)
                    if valid:
                        valid_moves.append((row, col, to_row, to_col, bool(captured)))
                
                # Check diagonally forward right
                to_row, to_col = row + direction, col + 1
                if is_valid_position(to_row, to_col):
                    valid, captured = is_valid_move(row, col, to_row, to_col, player)
                    if valid:
                        valid_moves.append((row, col, to_row, to_col, bool(captured)))
                
                # Check capture moves
                for dr in [direction * 2]:
                    for dc in [-2, 2]:
                        to_row, to_col = row + dr, col + dc
                        if is_valid_position(to_row, to_col):
                            valid, captured = is_valid_move(row, col, to_row, to_col, player)
                            if valid:
                                valid_moves.append((row, col, to_row, to_col, bool(captured)))
    
    return valid_moves

# Function to evaluate a position for the AI
def evaluate_position():
    human_pieces = sum(1 for row in board for cell in row if cell.strip('[]') == HUMAN)
    ai_pieces = sum(1 for row in board for cell in row if cell.strip('[]') == AI)
    
    # Count pieces in strategic positions (center of the board)
    strategic_ai_pieces = 0
    for row in range(2, 6):
        for col in range(2, 6):
            if board[row][col].strip('[]') == AI:
                strategic_ai_pieces += 1
    
    return {
        'human_pieces': human_pieces,
        'ai_pieces': ai_pieces,
        'material_advantage': ai_pieces - human_pieces,
        'strategic_position': strategic_ai_pieces
    }

# AI strategy implementations
def default_ai_strategy():
    valid_moves = get_valid_moves(AI)
    
    if not valid_moves:
        return None
    
    # Prioritize capture moves
    capture_moves = [move for move in valid_moves if move[4]]
    
    if capture_moves:
        return random.choice(capture_moves)[:4]  # Remove the captured flag
    else:
        return random.choice(valid_moves)[:4]  # Remove the captured flag

def aggressive_ai_strategy():
    valid_moves = get_valid_moves(AI)
    
    if not valid_moves:
        return None
    
    # Always prioritize capture moves
    capture_moves = [move for move in valid_moves if move[4]]
    
    if capture_moves:
        return random.choice(capture_moves)[:4]
    
    # If no captures available, move toward human pieces
    human_positions = []
    for row in range(rows):
        for col in range(cols):
            if board[row][col].strip('[]') == HUMAN:
                human_positions.append((row, col))
    
    if human_positions:
        # Find the move that gets closest to a human piece
        target = random.choice(human_positions)
        best_move = valid_moves[0]
        min_distance = 16  # Maximum possible distance on an 8x8 board
        
        for move in valid_moves:
            to_row, to_col = move[2], move[3]
            distance = abs(to_row - target[0]) + abs(to_col - target[1])
            if distance < min_distance:
                min_distance = distance
                best_move = move
        
        return best_move[:4]
    
    return random.choice(valid_moves)[:4]

def defensive_ai_strategy():
    valid_moves = get_valid_moves(AI)
    
    if not valid_moves:
        return None
    
    # Prioritize capture moves
    capture_moves = [move for move in valid_moves if move[4]]
    
    if capture_moves:
        return random.choice(capture_moves)[:4]
    
    # Calculate safety score for each move (how far from human pieces)
    human_positions = []
    for row in range(rows):
        for col in range(cols):
            if board[row][col].strip('[]') == HUMAN:
                human_positions.append((row, col))
    
    if human_positions:
        # Find the move that gets furthest from human pieces
        safest_moves = []
        max_safety = 0
        
        for move in valid_moves:
            to_row, to_col = move[2], move[3]
            min_distance = 16  # Maximum possible distance on an 8x8 board
            
            for h_row, h_col in human_positions:
                distance = abs(to_row - h_row) + abs(to_col - h_col)
                min_distance = min(min_distance, distance)
            
            if min_distance > max_safety:
                max_safety = min_distance
                safest_moves = [move]
            elif min_distance == max_safety:
                safest_moves.append(move)
        
        return random.choice(safest_moves)[:4]
    
    return random.choice(valid_moves)[:4]

def strategic_ai_strategy():
    valid_moves = get_valid_moves(AI)
    
    if not valid_moves:
        return None
    
    # Prioritize capture moves
    capture_moves = [move for move in valid_moves if move[4]]
    
    if capture_moves:
        return random.choice(capture_moves)[:4]
    
    # Calculate center-control score for each move
    center_moves = []
    best_center_score = -1
    
    for move in valid_moves:
        to_row, to_col = move[2], move[3]
        # Calculate how close to center (3.5, 3.5)
        center_score = 8 - (abs(to_row - 3.5) + abs(to_col - 3.5))
        
        if center_score > best_center_score:
            best_center_score = center_score
            center_moves = [move]
        elif center_score == best_center_score:
            center_moves.append(move)
    
    return random.choice(center_moves)[:4]

def chatgpt_ai_strategy():
    # ChatGPT strategy: look ahead and value both attack and defense
    valid_moves = get_valid_moves(AI)
    
    if not valid_moves:
        return None
    
    # Prioritize capture moves
    capture_moves = [move for move in valid_moves if move[4]]
    
    if capture_moves and random.random() < 0.85:  # 85% chance to take capture if available
        return random.choice(capture_moves)[:4]
    
    # Look ahead to see if move leads to capture or being captured
    best_moves = []
    best_score = -100
    
    for move in valid_moves:
        from_row, from_col, to_row, to_col = move[:4]
        score = 0
        
        # Make temporary move
        temp_piece = board[from_row][from_col]
        temp_dest = board[to_row][to_col]
        board[to_row][to_col] = temp_piece
        board[from_row][from_col] = '[ ]'
        
        # Check if this move exposes us to capture
        human_moves = get_valid_moves(HUMAN)
        human_captures = [m for m in human_moves if m[4]]
        
        if human_captures:
            score -= 5
        
        # Check if this move sets up future captures
        ai_future_moves = get_valid_moves(AI)
        ai_future_captures = [m for m in ai_future_moves if m[4]]
        
        if ai_future_captures:
            score += 3
        
        # Add positional value (center control)
        center_score = 8 - (abs(to_row - 3.5) + abs(to_col - 3.5))
        score += center_score * 0.5
        
        # Restore board
        board[from_row][from_col] = temp_piece
        board[to_row][to_col] = temp_dest
        
        if score > best_score:
            best_score = score
            best_moves = [move]
        elif score == best_score:
            best_moves.append(move)
    
    return random.choice(best_moves)[:4]

def gemini_ai_strategy():
    # Gemini strategy: mix of aggression, defense, and occasional surprising moves
    valid_moves = get_valid_moves(AI)
    
    if not valid_moves:
        return None
    
    # 10% chance of making a completely random move (surprise factor)
    if random.random() < 0.1:
        return random.choice(valid_moves)[:4]
    
    # Prioritize capture moves
    capture_moves = [move for move in valid_moves if move[4]]
    
    if capture_moves:
        return random.choice(capture_moves)[:4]
    
    # Combined strategy: evaluate moves based on multiple factors
    move_scores = []
    
    for move in valid_moves:
        from_row, from_col, to_row, to_col = move[:4]
        score = 0
        
        # Make temporary move
        temp_piece = board[from_row][from_col]
        temp_dest = board[to_row][to_col]
        board[to_row][to_col] = temp_piece
        board[from_row][from_col] = '[ ]'
        
        # Defense factor
        human_moves = get_valid_moves(HUMAN)
        human_captures = [m for m in human_moves if m[4]]
        if human_captures:
            score -= 4
        
        # Attack potential
        ai_future_moves = get_valid_moves(AI)
        ai_future_captures = [m for m in ai_future_moves if m[4]]
        if ai_future_captures:
            score += 3
        
        # Position factor
        # Center control
        center_score = 8 - (abs(to_row - 3.5) + abs(to_col - 3.5))
        score += center_score * 0.4
        
        # Forward progression (rewards advancing pieces)
        score += to_row * 0.5  # AI moves downward, so higher row is better
        
        # Restore board
        board[from_row][from_col] = temp_piece
        board[to_row][to_col] = temp_dest
        
        move_scores.append((move, score))
    
    # Get the moves with the highest scores
    move_scores.sort(key=lambda x: x[1], reverse=True)
    best_score = move_scores[0][1]
    best_moves = [m for m, s in move_scores if s >= best_score]
    
    return random.choice(best_moves)[:4]

# Function for AI to make a move
def ai_move():
    print(f"AI ({selected_ai}) is thinking...")
    time.sleep(1)  # Add a small delay to simulate thinking
    
    # Choose strategy based on selected AI
    if selected_ai == "Default":
        move = default_ai_strategy()
    elif selected_ai == "Aggressive":
        move = aggressive_ai_strategy()
    elif selected_ai == "Defensive":
        move = defensive_ai_strategy()
    elif selected_ai == "Strategic":
        move = strategic_ai_strategy()
    elif selected_ai == "ChatGPT":
        move = chatgpt_ai_strategy()
    elif selected_ai == "Gemini":
        move = gemini_ai_strategy()
    else:
        move = default_ai_strategy()
    
    if not move:
        print("AI has no valid moves. Human wins!")
        return False
    
    from_row, from_col, to_row, to_col = move
    print(f"AI moves from {column_labels[from_col]}{from_row+1} to {column_labels[to_col]}{to_row+1}")
    move_piece(from_row, from_col, to_row, to_col)
    return True

# Function to check if game is over
def check_game_over():
    # Check if any player has no pieces left
    human_pieces = sum(1 for row in board for cell in row if cell.strip('[]') == HUMAN)
    ai_pieces = sum(1 for row in board for cell in row if cell.strip('[]') == AI)
    
    if human_pieces == 0:
        print(f"Game over! AI ({selected_ai}) wins!")
        return True
    elif ai_pieces == 0:
        print("Game over! You win!")
        return True
    
    # Check if current player has no valid moves
    valid_moves = get_valid_moves(current_player)
    if not valid_moves:
        winner = "Human" if current_player == AI else f"AI ({selected_ai})"
        print(f"Game over! {winner} wins because opponent has no valid moves!")
        return True
    
    return False

# Function to show AI selection menu
def select_ai():
    global selected_ai
    print("\n=== Choose your AI opponent ===")
    for i, (ai_name, description) in enumerate(ai_types.items(), 1):
        print(f"{i}. {ai_name}: {description}")
    
    while True:
        try:
            choice = int(input(f"Enter your choice (1-{len(ai_types)}): "))
            if 1 <= choice <= len(ai_types):
                selected_ai = list(ai_types.keys())[choice - 1]
                print(f"You selected: {selected_ai}")
                break
            else:
                print(f"Please enter a number between 1 and {len(ai_types)}")
        except ValueError:
            print("Please enter a valid number")

# Main game function
def play_game():
    global current_player
    print("Welcome to Checkers! You are playing with '#' pieces.")
    
    # Select AI opponent
    select_ai()
    print(f"You are playing against {selected_ai} AI with '@' pieces.")
    print("To make a move, enter the coordinates (e.g., 'a6' for column a, row 6)")
    
    # Reset board
    reset_board()
    
    while True:
        print_board()
        
        if check_game_over():
            break
        
        if current_player == HUMAN:
            try:
                from_coord = input("Enter the coordinates of your piece (e.g., 'a6') or 'q' to quit: ")
                if from_coord.lower() == 'q':
                    print("Game ended by player.")
                    break
                    
                to_coord = input("Enter the coordinates where you want to move (e.g., 'b5'): ")
                
                from_col = ord(from_coord[0].lower()) - ord('a')
                from_row = int(from_coord[1]) - 1
                to_col = ord(to_coord[0].lower()) - ord('a')
                to_row = int(to_coord[1]) - 1
                
                if not is_valid_position(from_row, from_col) or not is_valid_position(to_row, to_col):
                    print("Invalid coordinates. Please enter coordinates within the board range.")
                    continue
                
                if not move_piece(from_row, from_col, to_row, to_col):
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Please use correct format (e.g., 'a6').")
                continue
        else:
            if not ai_move():
                break

# Main menu function
def main_menu():
    while True:
        print("\n==== CHECKERS GAME ====")
        print("1. Play Game")
        print("2. Rules")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            play_game()
            input("Press Enter to continue...")
        elif choice == "2":
            print("\n=== RULES ===")
            print("- You play as '#' pieces, AI plays as '@' pieces")
            print("- Move diagonally forward one square")
            print("- Capture by jumping over an opponent's piece diagonally")
            print("- The game ends when a player has no pieces left or cannot make a move")
            input("Press Enter to continue...")
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the game
if __name__ == "__main__":
    main_menu()