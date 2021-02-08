from random import choice

class tic_tac_toe:
	def __init__(self):
		self.grid_contents = [x for x in range(9)]
		self.rem_positions = [x for x in range(9)]
		self.winner = ''

	def display_grid(self):
		count = 0
		print('\t', end='')
		for x in self.grid_contents:
			print(f'| {x} ', end='')
			count += 1
			if count % 3 == 0:
				print('|\n\t', end='')
		print()

	def check_row_column_diagonal(self, *args):
		if self.grid_contents[args[0]] == self.grid_contents[args[1]] == self.grid_contents[args[2]] != ' ':
			self.winner = self.grid_contents[args[0]]
			return True
		else:
			return False

	def check_diagonals(self):
		if self.check_row_column_diagonal(*range(0, 9, 4)) or self.check_row_column_diagonal(*range(2, 8, 2)):
			return True
		else:
			return False

	def check_rows(self):
		a, b = 0, 3
		for x in range(3):
			if self.check_row_column_diagonal(*range(a, b)):
				return True
			a, b = b, b+3
		return False

	def check_columns(self):
		a, b = 0, 7
		for x in range(3):
			if self.check_row_column_diagonal(*range(a, b, 3)):
				return True
			a, b = a+1, b+1
		return False

	def win_lose(self):
		if self.check_columns() or self.check_rows() or self.check_diagonals():
			return 'Win'
		if ' ' in self.grid_contents:
			return 'continue'
		else:
			return 'Draw'

	def fill_position(self, grid_position, variable):
		self.grid_contents[grid_position] = variable
		self.rem_positions.remove(grid_position)

	def combined_func(self, position_tuple, move_count):
		self.fill_position(*position_tuple)
		self.display_grid()
		return move_count + 1

	def start_game(self):
		print('*** Lets Play Tic-Tac-Toe ***')
		self.display_grid()
		self.grid_contents = [' ']*9

		user_var = input('You wanna Play "X" or "O" : ')
		print()
		if user_var == 'X':
			comp_var = 'O'
		else:
			comp_var = 'X'

		move_count, game_end_status = 0, 'continue'
		while (game_end_status == 'continue'):
			user_position = int(input(f'Enter Position to place \'{user_var}\' : '))

			move_count = self.combined_func((user_position, user_var), move_count)

			if move_count > 4:
				game_end_status = self.win_lose()
				if game_end_status != 'continue':
					break

			comp_position = choice(self.rem_positions)
			print(f'Computer Plays \'{comp_var}\' at position {comp_position}')
			move_count = self.combined_func((comp_position, comp_var), move_count)

			if move_count > 4:
				game_end_status = self.win_lose()

		if game_end_status == 'Win':
			print(f'*** \'{self.winner}\' Wins ***')
		elif game_end_status == 'Draw':
			print('*** Ohh!!! It was a Draw. No One Wins ***')


game = tic_tac_toe()
game.start_game()
