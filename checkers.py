rows = 8
cols = 8

# Create the board with placeholders for empty spaces and initial positions for pieces
board = [['[ ]' for _ in range(cols)] for _ in range(rows)]

# Define initial positions of pieces
initial_positions = {
    (0, 1): 'R', (0, 3): 'R', (0, 5): 'R', (0, 7): 'R',
    (1, 0): 'R', (1, 2): 'R', (1, 4): 'R', (1, 6): 'R',
    (2, 1): 'R', (2, 3): 'R', (2, 5): 'R', (2, 7): 'R',
    (5, 0): 'B', (5, 2): 'B', (5, 4): 'B', (5, 6): 'B',
    (6, 1): 'B', (6, 3): 'B', (6, 5): 'B', (6, 7): 'B',
    (7, 0): 'B', (7, 2): 'B', (7, 4): 'B', (7, 6): 'B'
}

# Place pieces on the board
for (row, col), piece in initial_positions.items():
    board[row][col] = '[{}]'.format(piece)

# Define column labels
column_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Function to print the board with coordinates
def print_board():
    print("   " + "  ".join(column_labels))
    for i, row in enumerate(board, start=1):
        print(str(i) + " " + " ".join(row))

# Function to move a piece on the board
def move_piece(from_row, from_col, to_row, to_col):
    piece = board[from_row][from_col]
    if piece == '[ ]':
        print("No piece at the selected position.")
        return
    elif board[to_row][to_col] != '[ ]':
        print("The destination position is occupied.")
        return
    else:
        board[to_row][to_col] = piece
        board[from_row][from_col] = '[ ]'
        print("Piece moved successfully.")

# Main loop
while True:
    print_board()
    from_coord = input("Enter the coordinates of the piece you want to move (e.g., 'a2'): ")
    to_coord = input("Enter the coordinates where you want to move the piece (e.g., 'b3'): ")

    from_col = ord(from_coord[0]) - ord('a')
    from_row = int(from_coord[1]) - 1
    to_col = ord(to_coord[0]) - ord('a')
    to_row = int(to_coord[1]) - 1

    if 0 <= from_row < rows and 0 <= from_col < cols and 0 <= to_row < rows and 0 <= to_col < cols:
        move_piece(from_row, from_col, to_row, to_col)
    else:
        print("Invalid coordinates. Please enter coordinates within the board range.")