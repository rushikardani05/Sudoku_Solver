import tkinter as tk
from tkinter import messagebox

# Backtracking solver function
def solve_sudoku(grid):
    empty = find_empty(grid)
    if not empty:
        return True  # Solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, num, row, col):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Backtrack
    return False

def is_valid(grid, num, row, col):
    # Check row and column
    if any(grid[row][x] == num for x in range(9)) or any(grid[x][col] == num for x in range(9)):
        return False
    # Check 3x3 box
    box_row, box_col = row - row % 3, col - col % 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if grid[r][c] == num:
                return False
    return True

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

# GUI logic
def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            if val == "":
                row.append(0)
            elif val.isdigit() and 1 <= int(val) <= 9:
                row.append(int(val))
            else:
                messagebox.showerror("Invalid Input", "Only digits 1-9 allowed.")
                return None
        board.append(row)
    return board

def fill_board(board):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, str(board[i][j]))

def solve():
    board = get_board()
    if board:
        if solve_sudoku(board):
            fill_board(board)
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists!")

def clear():
    for row in entries:
        for cell in row:
            cell.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Sudoku Solver")
root.geometry("450x500")
root.configure(bg="#f9f9f9")

tk.Label(root, text="Sudoku Solver", font=("Arial", 16, "bold"), bg="#f9f9f9").pack(pady=10)

frame = tk.Frame(root, bg="#f9f9f9")
frame.pack()

entries = []
for i in range(9):
    row_entries = []
    for j in range(9):
        e = tk.Entry(frame, width=3, font=("Arial", 14), justify="center")
        e.grid(row=i, column=j, padx=2, pady=2)
        row_entries.append(e)
    entries.append(row_entries)

# Buttons
btn_frame = tk.Frame(root, bg="#f9f9f9")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Solve", width=10, bg="#4CAF50", fg="white", command=solve).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear", width=10, bg="#f44336", fg="white", command=clear).grid(row=0, column=1, padx=10)

root.mainloop()
