# Aleksander Popovic
# Last Updated: 12/24/2021

from tkinter import *
from sudoku import Board

# Set up

root = Tk()
root.configure(bg="#ccfcff")
root.title("Sudoku")
root.geometry("850x550")
active_row = IntVar(value=-1)
active_col = IntVar(value=-1)
correct_nums_placed = IntVar(value=0)

# Functions

def get_row(row):

	return squares[row]
	
def get_col(col):

    return [squares[r][col] for r in range(len(squares))]

def get_subgrid(row, col):

    return [squares[r][c] for r in subgrids[row // 3] for c in subgrids[col // 3]]

def click_square(row, col):

    active_row.set(row)
    active_col.set(col)
    for r in range(9):
        for c in range(9):
            if r == row and col == c:
                squares[r][c].configure(bg="#fcff40")
            elif squares[r][c] in get_row(row) or squares[r][c] in get_col(col) or squares[r][c] in get_subgrid(row, col):
                squares[r][c].configure(bg="#feffd4")
            elif squares[r][c] in gray_squares:
                squares[r][c].configure(bg="#c7c9c8")
            else:
                squares[r][c].configure(bg="white")

def right_click_square(self):

    active_row.set(value=-1)
    active_col.set(value=-1)
    for r in range(9):
        for c in range(9):
            if squares[r][c] in gray_squares:
                squares[r][c].configure(bg="#c7c9c8")
            else:
                squares[r][c].configure(bg="white")

def press1(self):

    row = active_row.get()
    col = active_col.get()
    if row < 0 or row > 8:
        message.configure(text="Message: Please select a square first.")
    elif squares[row][col].cget("state") == DISABLED:
        message.configure(text="Message: You cannot change one of the starting squares.")
    elif squares[row][col].cget("text") == "1":
        pass
    elif b2.board[row][col] == 1:
        squares[row][col].configure(text="1", fg="blue")
        correct_nums_placed.set(correct_nums_placed.get() + 1)
        message.configure(text="Message:")
        check_for_winner()
    else:
        if squares[row][col].cget("text") == "":
            pass
        elif int(squares[row][col].cget("text")) == b2.board[row][col]:
            correct_nums_placed.set(correct_nums_placed.get() - 1)
        squares[row][col].configure(text="1", fg="red")
        message.configure(text="Message:")

def press2(self):

    row = active_row.get()
    col = active_col.get()
    if row < 0 or row > 8:
        message.configure(text="Message: Please select a square first.")
    elif squares[row][col].cget("state") == DISABLED:
        message.configure(text="Message: You cannot change one of the starting squares.")
    elif squares[row][col].cget("text") == "2":
        pass
    elif b2.board[row][col] == 2:
        squares[row][col].configure(text="2", fg="blue")
        correct_nums_placed.set(correct_nums_placed.get() + 1)
        message.configure(text="Message:")
        check_for_winner()
    else:
        if squares[row][col].cget("text") == "":
            pass
        elif int(squares[row][col].cget("text")) == b2.board[row][col]:
            correct_nums_placed.set(correct_nums_placed.get() - 1)
        squares[row][col].configure(text="2", fg="red")
        message.configure(text="Message:")

def press3(self):

    row = active_row.get()
    col = active_col.get()
    if row < 0 or row > 8:
        message.configure(text="Message: Please select a square first.")
    elif squares[row][col].cget("state") == DISABLED:
        message.configure(text="Message: You cannot change one of the starting squares.")
    elif squares[row][col].cget("text") == "3":
        pass
    elif b2.board[row][col] == 3:
        squares[row][col].configure(text="3", fg="blue")
        correct_nums_placed.set(correct_nums_placed.get() + 1)
        message.configure(text="Message:")
        check_for_winner()
    else:
        if squares[row][col].cget("text") == "":
            pass
        elif int(squares[row][col].cget("text")) == b2.board[row][col]:
            correct_nums_placed.set(correct_nums_placed.get() - 1)
        squares[row][col].configure(text="3", fg="red")
        message.configure(text="Message:")

def press4(self):

    row = active_row.get()
    col = active_col.get()
    if row < 0 or row > 8:
        message.configure(text="Message: Please select a square first.")
    elif squares[row][col].cget("state") == DISABLED:
        message.configure(text="Message: You cannot change one of the starting squares.")
    elif squares[row][col].cget("text") == "4":
        pass
    elif b2.board[row][col] == 4:
        squares[row][col].configure(text="4", fg="blue")
        correct_nums_placed.set(correct_nums_placed.get() + 1)
        message.configure(text="Message:")
        check_for_winner()
    else:
        if squares[row][col].cget("text") == "":
            pass
        elif int(squares[row][col].cget("text")) == b2.board[row][col]:
            correct_nums_placed.set(correct_nums_placed.get() - 1)
        squares[row][col].configure(text="4", fg="red")
        message.configure(text="Message:")

def press5(self):

    row = active_row.get()
    col = active_col.get()
    if row < 0 or row > 8:
        message.configure(text="Message: Please select a square first.")
    elif squares[row][col].cget("state") == DISABLED:
        message.configure(text="Message: You cannot change one of the starting squares.")
    elif squares[row][col].cget("text") == "5":
        pass
    elif b2.board[row][col] == 5:
        squares[row][col].configure(text="5", fg="blue")
        correct_nums_placed.set(correct_nums_placed.get() + 1)
        message.configure(text="Message:")
        check_for_winner()
    else:
        if squares[row][col].cget("text") == "":
            pass
        elif int(squares[row][col].cget("text")) == b2.board[row][col]:
            correct_nums_placed.set(correct_nums_placed.get() - 1)
        squares[row][col].configure(text="5", fg="red")
        message.configure(text="Message:")

def press6(self):

    row = active_row.get()
    col = active_col.get()
    if row < 0 or row > 8:
        message.configure(text="Message: Please select a square first.")
    elif squares[row][col].cget("state") == DISABLED:
        message.configure(text="Message: You cannot change one of the starting squares.")
    elif squares[row][col].cget("text") == "6":
        pass
    elif b2.board[row][col] == 6:
        squares[row][col].configure(text="6", fg="blue")
        correct_nums_placed.set(correct_nums_placed.get() + 1)
        message.configure(text="Message:")
        check_for_winner()
    else:
        if squares[row][col].cget("text") == "":
            pass
        elif int(squares[row][col].cget("text")) == b2.board[row][col]:
            correct_nums_placed.set(correct_nums_placed.get() - 1)
        squares[row][col].configure(text="6", fg="red")
        message.configure(text="Message:")

def press7(self):

    row = active_row.get()
    col = active_col.get()
    if row < 0 or row > 8:
        message.configure(text="Message: Please select a square first.")
    elif squares[row][col].cget("state") == DISABLED:
        message.configure(text="Message: You cannot change one of the starting squares.")
    elif squares[row][col].cget("text") == "7":
        pass
    elif b2.board[row][col] == 7:
        squares[row][col].configure(text="7", fg="blue")
        correct_nums_placed.set(correct_nums_placed.get() + 1)
        message.configure(text="Message:")
        check_for_winner()
    else:
        if squares[row][col].cget("text") == "":
            pass
        elif int(squares[row][col].cget("text")) == b2.board[row][col]:
            correct_nums_placed.set(correct_nums_placed.get() - 1)
        squares[row][col].configure(text="7", fg="red")
        message.configure(text="Message:")

def press8(self):

    row = active_row.get()
    col = active_col.get()
    if row < 0 or row > 8:
        message.configure(text="Message: Please select a square first.")
    elif squares[row][col].cget("state") == DISABLED:
        message.configure(text="Message: You cannot change one of the starting squares.")
    elif squares[row][col].cget("text") == "8":
        pass
    elif b2.board[row][col] == 8:
        squares[row][col].configure(text="8", fg="blue")
        correct_nums_placed.set(correct_nums_placed.get() + 1)
        message.configure(text="Message:")
        check_for_winner()
    else:
        if squares[row][col].cget("text") == "":
            pass
        elif int(squares[row][col].cget("text")) == b2.board[row][col]:
            correct_nums_placed.set(correct_nums_placed.get() - 1)
        squares[row][col].configure(text="8", fg="red")
        message.configure(text="Message:")

def press9(self):

    row = active_row.get()
    col = active_col.get()
    if row < 0 or row > 8:
        message.configure(text="Message: Please select a square first.")
    elif squares[row][col].cget("state") == DISABLED:
        message.configure(text="Message: You cannot change one of the starting squares.")
    elif squares[row][col].cget("text") == "9":
        pass
    elif b2.board[row][col] == 9:
        squares[row][col].configure(text="9", fg="blue")
        correct_nums_placed.set(correct_nums_placed.get() + 1)
        message.configure(text="Message:")
        check_for_winner()
    else:
        if squares[row][col].cget("text") == "":
            pass
        elif int(squares[row][col].cget("text")) == b2.board[row][col]:
            correct_nums_placed.set(correct_nums_placed.get() - 1)
        squares[row][col].configure(text="9", fg="red")
        message.configure(text="Message:")

def press_backspace(self):

    row = active_row.get()
    col = active_col.get()
    if row < 0 or row > 8:
        message.configure(text="Message: Please select a square first.")
    elif squares[row][col].cget("state") == DISABLED:
        message.configure(text="Message: You cannot delete one of the starting squares.")
    else:
        if squares[row][col].cget("text") == "":
            pass
        elif int(squares[row][col].cget("text")) == b2.board[row][col]:
            correct_nums_placed.set(correct_nums_placed.get() - 1)
        squares[row][col].configure(text="", fg="blue")
        message.configure(text="Message:")

def press_up(self):

    row = active_row.get()
    col = active_col.get()
    if correct_nums_placed.get() == 81:
        pass
    elif row < 0 or row > 8:
        message.configure(text="Message: Please select a square first.")
    elif row > 0:
        row = row - 1
        click_square(row, col)

def press_down(self):

    row = active_row.get()
    col = active_col.get()
    if correct_nums_placed.get() == 81:
        pass
    elif row < 0 or row > 8:
        message.configure(text="Message: Please select a square first.")
    elif row < 8:
        row = row + 1
        click_square(row, col)

def press_left(self):

    row = active_row.get()
    col = active_col.get()
    if correct_nums_placed.get() == 81:
        pass
    elif row < 0 or row > 8:
        message.configure(text="Message: Please select a square first.")
    elif col > 0:
        col = col - 1
        click_square(row, col)

def press_right(self):

    row = active_row.get()
    col = active_col.get()
    if correct_nums_placed.get() == 81:
        pass
    elif row < 0 or row > 8:
        message.configure(text="Message: Please select a square first.")
    elif col < 8:
        col = col + 1
        click_square(row, col)

def check_for_winner():

    if correct_nums_placed.get() == 81:
        right_click_square(0)
        for r in range(9):
            for c in range(9):
                squares[r][c].configure(state=DISABLED)
        message.configure(text="Message: You won. Congratulations!")
        solve_button.configure(state=DISABLED)

def create_new_board():

    right_click_square(0)
    global b
    b = Board()
    b.set_start_squares()
    correct_nums_placed.set(value=b.nums_placed)
    global b2
    b2 = Board(b.board, b.nums_placed)
    b2.depth_first_solve()
    message.configure(text="Message:")
    solve_button.configure(state=NORMAL)
    for r in range(9):
        for c in range(9):
            if type(b.board[r][c]) == int:
                squares[r][c].configure(text=b.board[r][c], state=DISABLED, fg="black")
            else:
                squares[r][c].configure(text="", state=NORMAL, fg="blue")

def solve():

    if clicked.get() == "Depth First":
        b.depth_first_solve()
    elif clicked.get() == "Breadth First":
        b.breadth_first_solve()
    elif clicked.get() == "Recursive Depth First":
        b.recursive_depth_first_solve()
    else:
        b.recursive_breadth_first_solve()
    for r in range(9):
        for c in range(9):
            if squares[r][c].cget("state") == NORMAL:
                squares[r][c].configure(text=str(b.board[r][c]))
    correct_nums_placed.set(value=81)
    check_for_winner()

# Widgets, Bindings, and Placements on screen

space = Label(root, bg="#ccfcff", text="        ")
space.grid(row=0, column=0)

title = Label(root, text="Play Sudoku", bg="#ccfcff", font=("Arial", 20), pady=20)
title.grid(row=0, column=1, columnspan=11)

instructions_header = Label(root, text="Instructions", bg="#ccfcff", font=("Arial", 15))
instructions_header.grid(row=1, column=11)

instructions = Label(root, bg="#ccfcff", justify=LEFT, padx=25, font=("Arial", 12),
    text="* Click on a square to select it.\n* Use the arrow keys to move from square to square.\n"
    + "* Use the number keys to select the number.\n* Use the backspace key to delete a number from a square.\n"
    + "* Red numbers are in the incorrect place.\n* Blue numbers are correct.\n"
    + '* If you would like to solve the puzzle, choose\n  a method from the dropdown and press "Solve."\n'
    + '* Press "New Game" to play again.')
instructions.grid(row=2, column=11, rowspan=5)

new_game = Button(root, text="New Game", height=2, width=12, command=create_new_board)
new_game.grid(row=7, column=11)

solve_options = ["Depth First", "Breadth First", "Recursive Depth First", "Recursive Breadth First"]
clicked = StringVar(value=solve_options[0])
dropdown = OptionMenu(root, clicked, *solve_options)
dropdown.grid(row=9, column=11)
solve_button = Button(root, text="Solve", height=2, width=12, command=solve)
solve_button.grid(row=8, column=11)

message = Label(root, bg="#ccfcff", pady=20, font=("Arial", 10), text="Message:")
message.grid(row=12, column=1, columnspan=9, sticky=W)

subgrids = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
squares = [[Button(root, height=2, width=4, relief="ridge", fg="blue", command=lambda x=c, y=r: click_square(x, y))
    for r in range(9)] for c in range(9)]
gray_squares = get_subgrid(0, 0) + get_subgrid(0, 6) + get_subgrid(3, 3) + get_subgrid(6, 0) + get_subgrid(6, 6)

for square in gray_squares:
    square.configure(bg="#c7c9c8")
for r in range(9):
    for c in range(9):
        squares[r][c].bind("<Button-3>", right_click_square)
        squares[r][c].grid(row=r+1, column=c+1)

root.bind("1", press1)
root.bind("2", press2)
root.bind("3", press3)
root.bind("4", press4)
root.bind("5", press5)
root.bind("6", press6)
root.bind("7", press7)
root.bind("8", press8)
root.bind("9", press9)
root.bind("<BackSpace>", press_backspace)
root.bind("<Up>", press_up)
root.bind("<Down>", press_down)
root.bind("<Left>", press_left)
root.bind("<Right>", press_right)

create_new_board()
root.mainloop()
