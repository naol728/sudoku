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