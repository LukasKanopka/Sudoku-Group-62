import math, random
import pygame


# This was inspired and adapted by "Program for Sudoku Generator" by Aarti Rathi and Ankur Trisal in website GeeksforGeeks
# Link is https://www.geeksforgeeks.org/program-sudoku-generator/
class SudokuGenerator:
    # Constructor method for class.
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = []
        self.box_length = int(math.sqrt(row_length))
        # Initializes the board with zeros.
        for i in range(0, self.row_length):
            rows = []
            for j in range(0, row_length):import math, random
import copy


# This was inspired and adapted by "Program for Sudoku Generator" by Aarti Rathi and Ankur Trisal in website GeeksforGeeks
# Link is https://www.geeksforgeeks.org/program-sudoku-generator/
class SudokuGenerator:
    # Constructor method for class.
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = []
        self.box_length = int(math.sqrt(row_length))
        # Initializes the board with zeros.
        for i in range(0, self.row_length):
            rows = []
            for j in range(0, row_length):
                rows.append(0)
            self.board.append(rows)
    # Returns a 2D python list of numbers, which represents the board.
    def get_board(self):
        return self.board
    # Displays board to console.
    def print_board(self):
        for i in self.board:
            for j in i:
                print(j, end=" ")
            print()
    # Checks if num is contained in the given row of the board.
    def valid_in_row(self, row, num):
        for val in range(self.row_length):
            if self.board[row][val] == num:
                return False
        return True
    # Checks if num is contained in the given column of the board.
    def valid_in_col(self, col, num):
        for val in range(0, self.row_length):
            if self.board[val][col] == num:
                return False
        return True
    # Determines if num is contained in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)
    def valid_in_box(self, row_start, col_start, num):
        for val in range(0, self.box_length):
            for i in range(0, self.box_length):
                if self.board[row_start + val][col_start + i] == num:
                    return False
        return True
    # Returns if it is valid to enter num at (row, col) in the board by checking row, column, and box.
    def is_valid(self, row, col, num):
        if not self.valid_in_row(row, num):
            return False
        if not self.valid_in_col(col, num):
            return False
        row_start = row // 3
        row_start *= 3
        col_start = col // 3
        col_start *= 3
        if not self.valid_in_box(row_start, col_start, num):
            return False
        return True
    # Randomly fills in values in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)
    def fill_box(self, row_start, col_start):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                check = True
                # Constantly checks a random number until it is valid for the box.
                while check:
                    num = random.randint(1, 9)
                    if self.valid_in_box(row_start, col_start, num):
                        check = False
                self.board[i][j] = num
    # Fills the three boxes along diagonal of board.
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)
    # This method is provided for students. Returns a completely filled board.
    # From Professor
    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        # Determines the starting point for each box based on the current row.
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        # Tries filling numbers from 1 to 9 in the current position.
        for i in range(1, self.row_length + 1):
            if self.is_valid(row, col, i):
                self.board[row][col] = i
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False
    # This method is provided for students.
    # From professor.
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
    # Method to remove the appropriate number of cells from the board.
    def remove_cells(self):
        for j in range(self.removed_cells):
            r = random.randint(0, 8)
            c = random.randint(0,8)
            # Checks if the cell is already empty.
            if self.board[r][c] == 0:
                no = True
                while no:
                    r = random.randint(0, 8)
                    c = random.randint(0, 8)
                    # Finds a cell that is not empty.
                    if self.board[r][c] != 0:
                        no = False
            # Removes the value from the cell.
            self.board[r][c] = 0
# Calls methods and constructor from class.
# From professor.
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    solved_board = copy.deepcopy(board)
    sudoku.remove_cells()
    board = sudoku.get_board()
    return solved_board, board

                rows.append(0)
            self.board.append(rows)
    # Returns a 2D python list of numbers, which represents the board.
    def get_board(self):
        return self.board
    # Displays board to console.
    def print_board(self):
        for i in self.board:
            for j in i:
                print(j, end=" ")
            print()
    # Checks if num is contained in the given row of the board.
    def valid_in_row(self, row, num):
        for val in range(self.row_length):
            if self.board[row][val] == num:
                return False
        return True
    # Checks if num is contained in the given column of the board.
    def valid_in_col(self, col, num):
        for val in range(0, self.row_length):
            if self.board[val][col] == num:
                return False
        return True
    # Determines if num is contained in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)
    def valid_in_box(self, row_start, col_start, num):
        for val in range(0, self.box_length):
            for i in range(0, self.box_length):
                if self.board[row_start + val][col_start + i] == num:
                    return False
        return True
    # Returns if it is valid to enter num at (row, col) in the board by checking row, column, and box.
    def is_valid(self, row, col, num):
        if not self.valid_in_row(row, num):
            return False
        if not self.valid_in_col(col, num):
            return False
        row_start = row // 3
        row_start *= 3
        col_start = col // 3
        col_start *= 3
        if not self.valid_in_box(row_start, col_start, num):
            return False
        return True
    # Randomly fills in values in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)
    def fill_box(self, row_start, col_start):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                check = True
                # Constantly checks a random number until it is valid for the box.
                while check:
                    num = random.randint(1, 9)
                    if self.valid_in_box(row_start, col_start, num):
                        check = False
                self.board[i][j] = num
    # Fills the three boxes along diagonal of board.
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)
    # This method is provided for students. Returns a completely filled board.
    # From Professor
    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        # Determines the starting point for each box based on the current row.
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        # Tries filling numbers from 1 to 9 in the current position.
        for i in range(1, self.row_length + 1):
            if self.is_valid(row, col, i):
                self.board[row][col] = i
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False
    # This method is provided for students.
    # From professor.
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
    # Method to remove the appropriate number of cells from the board.
    def remove_cells(self):
        for j in range(self.removed_cells):
            r = random.randint(0, 8)
            c = random.randint(0,8)
            # Checks if the cell is already empty.
            if self.board[r][c] == 0:
                no = True
                while no:
                    r = random.randint(0, 8)
                    c = random.randint(0, 8)
                    # Finds a cell that is not empty.
                    if self.board[r][c] != 0:
                        no = False
            # Removes the value from the cell.
            self.board[r][c] = 0
# Calls methods and constructor from class.
# From professor.
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


