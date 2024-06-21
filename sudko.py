def create_board():
  """Initializes a blank Sudoku board."""
  board = [[0 for _ in range(9)] for _ in range(9)]
  return board

def display_board(board):
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