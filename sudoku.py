# Aleksander Popovic
# Last Updated: 12/24/2021

import random

class Board:
	
	def __init__(self, board = None, nums_placed = None):

		self.SIZE = 9
		self.SUBGRIDS = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]

		if board: # makes deep copy of board
			self.board = []
			for r in range(len(board)):
				new_row = []
				for c in range(len(board[r])):
					if type(board[r][c]) == int:
						new_row.append(board[r][c])
					else:
						new_row.append(board[r][c].copy())
				self.board.append(new_row)
		else:
			self.board = [[[num + 1 for num in range(self.SIZE)] for _ in range(self.SIZE)] for _ in range(self.SIZE)]
		
		if nums_placed:
			self.nums_placed = nums_placed
		else:
			self.nums_placed = 0
	
	def __str__(self):

		return f"nums placed: {self.nums_placed}, size: {self.SIZE}, subgrids: {self.SUBGRIDS}\n{self.board}"
	
	def rand_fill_board(self): # only used to test code

		for r in range(len(self.board)):
			for c in range(len(self.board[r])):
				self.board[r][c] = random.randint(1, self.SIZE)
				self.nums_placed += 1
	
	def get_row(self, row):

		return self.board[row]
	
	def get_col(self, col):

		return [self.board[r][col] for r in range(len(self.board))]

	def get_subgrid(self, row, col):

		return [self.board[r][c] for r in self.SUBGRIDS[row // 3] for c in self.SUBGRIDS[col // 3]]
	
	def get_subgrid_coords(self, row, col):

		return [(r, c) for r in self.SUBGRIDS[row // 3] for c in self.SUBGRIDS[col // 3]]
	
	def get_all_rows(self):

		return self.board
	
	def get_all_cols(self):

		return [self.get_col(c) for c in range(len(self.board[0]))]
	
	def get_all_subgrids(self):

		return [self.get_subgrid(r, c) for r in range(0, len(self.board), 3) for c in range(0, len(self.board[r]), 3)]

	def update(self, row, col, num):
		
		if type(self.board[row][col]) != int and num in self.board[row][col]:
			self.board[row][col] = num
			self.nums_placed += 1
			changed = []

			for c in range(len(self.get_row(row))):
				if type(self.board[row][c]) != int and num in self.board[row][c]:
					self.board[row][c].remove(num)
					changed.append((row, c))

			for r in range(len(self.get_col(col))):
				if type(self.board[r][col]) != int and num in self.board[r][col]:
					self.board[r][col].remove(num)
					changed.append((r, col))

			for (r, c) in self.get_subgrid_coords(row, col):
				if type(self.board[r][c]) != int and num in self.board[r][c]:
					self.board[r][c].remove(num)
					changed.append((r, c))

			return changed

		return None
	
	def revert(self, row, col, lst, changed): # opposite of update
		
		if type(self.board[row][col]) == int:
			num = self.board[row][col]
			self.board[row][col] = lst
			self.nums_placed -= 1

			for (r, c) in changed:
				self.board[r][c].append(num)
				self.board[r][c].sort()

			return True
		return False
	
	def remove_guess(self, row, col):

		if type(self.board[row][col]) == int:
			guess = self.board[row][col]
			self.board[row][col] = -1
			self.nums_placed -= 1
			options = list(range(1, 10))

			whole_col = self.get_col(col)
			for num in options:
				if num in whole_col:
					options.remove(num)
			for r in range(len(whole_col)):
				if type(whole_col[r]) != int and guess not in self.get_row(r) and guess not in self.get_subgrid(r, col):
					whole_col[r].append(guess)
					whole_col[r].sort()
			
			whole_row = self.get_row(row)
			for num in options:
				if num in whole_row:
					options.remove(num)
			for c in range(len(whole_row)):
				if type(whole_row[c]) != int and guess not in self.get_col(c) and guess not in self.get_subgrid(row, c):
					whole_row[c].append(guess)
					whole_row[c].sort()
			
			subgrid = self.get_subgrid(row, col)
			for num in options:
				if num in subgrid:
					options.remove(num)
			coords = self.get_subgrid_coords(row, col)
			for (r, c) in coords:
				if type(self.board[r][c]) != int and guess not in self.get_row(r) and guess not in self.get_col(c):
					self.board[r][c].append(guess)
					self.board[r][c].sort()

			self.board[row][col] = options
			return True
		return False
	
	def has_won(self):

		return self.nums_placed == 81
	
	def has_lost(self):
		
		for r in range(len(self.board)):
			for c in range(len(self.board[r])):
				if not self.board[r][c]:
					return True
		return False

	def print_pretty(self):

		string = ""
		for r in range(len(self.board)):
			for c in range(len(self.board[r])):
				if type(self.board[r][c]) == int:
					string += str(self.board[r][c]) + ' '
				else:
					string += '* '
				if c % 3 == 2 and c < 8:
					string += "| "
			string = string.strip() + '\n'
			if r % 3 == 2 and r < 8:
				string += ("-" * 21) + '\n'
		return string.strip()
	
	def most_constrained_square(self):
		
		square = [0] * 10
		coord = (-1, -1)
		for r in range(len(self.board)):
			for c in range(len(self.board[r])):
				if type(self.board[r][c]) != int and len(self.board[r][c]) < len(square):
					square = self.board[r][c]
					coord = (r, c)
		return coord
	
	def depth_first_solve(self): # guesses nums in descending order

		stack = [Board(self.board, self.nums_placed)]
		while not stack[-1].has_won():
			if stack[-1].has_lost():
				stack.pop()
				(r, c) = stack[-1].most_constrained_square()
				stack[-1].board[r][c].pop()
			else:
				new_board = Board(stack[-1].board, stack[-1].nums_placed)
				(r, c) = new_board.most_constrained_square()
				num = new_board.board[r][c][-1]
				new_board.update(r, c, num)
				stack.append(new_board)
		self.board = stack[-1].board
		self.nums_placed = stack[-1].nums_placed
	
	def breadth_first_solve(self): # guesses nums in ascending order

		queue = [Board(self.board, self.nums_placed)]
		while not queue[0].has_won():
			if queue[0].has_lost():
				queue.pop(0)
			else:
				new_board = Board(queue[0].board, queue[0].nums_placed)
				(r, c) = new_board.most_constrained_square()
				num = new_board.board[r][c][0]
				new_board.update(r, c, num)
				queue.append(new_board)
				queue[0].board[r][c].pop(0)
		self.board = queue[0].board
		self.nums_placed = queue[0].nums_placed

	def recursive_depth_first_solve(self): # guesses nums in ascending order

		if self.has_won():
			return True

		(r, c) = self.most_constrained_square()
		square = self.board[r][c]

		for num in square:
			changed = self.update(r, c, num)
			if self.recursive_depth_first_solve():
				return True
			else:
				self.revert(r, c, square, changed)

		return False

	def recursive_breadth_first_solve(self): # guesses nums in descending order

		def helper(board1: Board):

			if board1.has_won():
				self.board = board1.board
				self.nums_placed = board1.nums_placed
				return True

			if not board1.has_lost():
				(r, c) = board1.most_constrained_square()
				square = board1.board[r][c]
				num = square[-1]
				changed = board1.update(r, c, num)
				square.pop()
				board2 = Board(board1.board, board1.nums_placed)
				board2.revert(r, c, square.copy(), changed)

				if helper(board2) or helper(board1):
					return True

			return False
		
		return helper(self)
	
	def check_unique_solution(self): # depth first, fastest

		stack = [Board(self.board, self.nums_placed)]
		num_wins = 0
		while stack:
			if num_wins > 1:
				return False
			elif stack[-1].has_won():
				self.board = stack[-1].board
				self.nums_placed = stack[-1].nums_placed
				num_wins += 1
				stack.pop()
				if not stack:
					return num_wins == 1
				(r, c) = stack[-1].most_constrained_square()
				stack[-1].board[r][c].pop()
			elif stack[-1].has_lost():
				stack.pop()
				if not stack:
					return num_wins == 1
				(r, c) = stack[-1].most_constrained_square()
				stack[-1].board[r][c].pop()
			else:
				new_board = Board(stack[-1].board, stack[-1].nums_placed)
				(r, c) = new_board.most_constrained_square()
				num = new_board.board[r][c][-1]
				new_board.update(r, c, num)
				stack.append(new_board)
		return num_wins == 1
	
	def set_start_squares(self):

		self.board = [[[num + 1 for num in range(self.SIZE)] for _ in range(self.SIZE)] for _ in range(self.SIZE)]
		self.nums_placed = 0

		free_squares = [(r, c) for r in range(len(self.board)) for c in range(len(self.board[r]))]
		random.shuffle(free_squares)
		for (r, c) in free_squares:
			nums = list(range(1, 10))
			random.shuffle(nums)
			num = nums.pop()
			changed = self.update(r, c, num)
			while not self.recursive_depth_first_solve():
				self.revert(r, c, nums, changed)
				num = nums.pop()
				changed = self.update(r, c, num)
		
		random.shuffle(free_squares)
		for (r, c) in free_squares:
			board1 = Board(self.board, self.nums_placed)
			board1.remove_guess(r, c)
			if board1.check_unique_solution():
				self.remove_guess(r, c)

# TESTS
# check user input outside of class

# b = Board()
# print(b.print_pretty())

# b.set_start_squares()
# print('\n' + b.print_pretty())

# b2 = Board(b.board, b.nums_placed)
# b3 = Board(b.board, b.nums_placed)
# b4 = Board(b.board, b.nums_placed)

# b.depth_first_solve()
# b2.breadth_first_solve()
# b3.recursive_depth_first_solve()
# b4.recursive_breadth_first_solve()

# print('\n' + b.print_pretty())
# print('\n' + b2.print_pretty())
# print('\n' + b3.print_pretty())
# print('\n' + b4.print_pretty())
