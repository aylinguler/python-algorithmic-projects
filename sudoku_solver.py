# Sudoku Solver using Backtracking Algorithm.
# Implements an object-oriented approach to solve a standard 9x9 Sudoku puzzle.
# The solver uses recursion and constraint validation to fill empty cells.


class Board:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i != 0 else '*' for i in row]
            board_str += ' '.join(row_str) + '\n'
        return board_str

    def find_empty_cell(self):
        for row_index, row in enumerate(self.board):
            for col_index, value in enumerate(row):
                if value == 0:
                    return row_index, col_index
        return None

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3

        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if self.board[r][c] == num:
                    return False
        return True

    def is_valid(self, position, num):
        row, col = position

        return (
            self.valid_in_row(row, num) and
            self.valid_in_col(col, num) and
            self.valid_in_square(row, col, num)
        )

    def solver(self):
        empty = self.find_empty_cell()

        if not empty:
            return True  # Puzzle solved

        row, col = empty

        for guess in range(1, 10):
            if self.is_valid((row, col), guess):
                self.board[row][col] = guess

                if self.solver():
                    return True

                self.board[row][col] = 0  # Backtrack

        return False


def solve_sudoku(board):
    game = Board(board)

    print("Puzzle to solve:")
    print(game)

    if game.solver():
        print("Solved puzzle:")
        print(game)
    else:
        print("The provided puzzle is unsolvable.")

    return game


if __name__ == "__main__":
    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    solve_sudoku(puzzle)