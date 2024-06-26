def create_board():
  """Initializes a blank Sudoku board."""
  board = [[0 for _ in range(9)] for _ in range(9)]
  return board

def display_board(board):
  """Prints the Sudoku board in a readable format."""
  for i in range(9):
    for j in range(9):
      print(board[i][j], end=" ")
      if (j + 1) % 3 == 0:
        print("|", end=" ")
    print()
    if (i + 1) % 3 == 0:
      print("-" * 27)

def find_empty_cell(board):
  """Finds an empty cell in the Sudoku board."""
  for row in range(9):
    for col in range(9):
      if board[row][col] == 0:
        return row, col
  return None

def is_valid(board, row, col, num):
  """Checks if placing a number in a cell is valid according to Sudoku rules."""
  # Check row
  for i in range(9):
    if board[row][i] == num and col != i:
      return False
  # Check column
  for i in range(9):
    if board[i][col] == num and row != i:
      return False
  # Check subgrid
  start_row = (row // 3) * 3
  start_col = (col // 3) * 3
  for i in range(3):
    for j in range(3):
      if board[start_row + i][start_col + j] == num and (row, col) != (start_row + i, start_col + j):
        return False
  return True

def solve_sudoku(board):
  """Solves the Sudoku puzzle using backtracking."""
  empty_cell = find_empty_cell(board)
  # If no empty cell found, the board is solved
  if empty_cell is None:
    return True
  row, col = empty_cell

  # Try all numbers from 1 to 9
  for i in range(1, 10):
    if is_valid(board, row, col, i):
      board[row][col] = i
      if solve_sudoku(board):
        return True
      board[row][col] = 0  # Backtrack if placement doesn't lead to a solution

  return False

# Example usage
board = create_board()
# Pre-fill some cells (optional)
board[0][0] = 5
board[1][2] = 6
# ...

display_board(board)
solve_sudoku(board)
print("Solved Board:")
display_board(board)




