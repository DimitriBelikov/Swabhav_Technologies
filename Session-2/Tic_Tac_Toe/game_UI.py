from game_logic import game_logic
from random import choice

class game:
	def __init__(self):
		self.game_end_status = 'continue'
		self.logic_obj = game_logic()
	
	def display_grid(self): #Display Grid
		count = 0
		print('\t', end='')
		for x in self.logic_obj.grid_contents:
			print(f'| {x} ', end='')
			count += 1
			if count % 3 == 0:
				print('|\n\t', end='')
		print()
	
	def user_comp_variable(self):  # Accept User's Variable Choice
		user_var = input('You wanna Play "X" or "O" : ')
		if user_var == 'X':
			return(user_var, 'O')
		else:
			return(user_var, 'X')
	
	def display_result(self): #Display Result when Done
		if self.game_end_status == 'Win':
			print(f'*** \'{self.logic_obj.winner}\' Wins ***')
		elif self.game_end_status == 'Draw':
			print('*** Ohh!!! It was a Draw. No One Wins ***')
	
	def start_game(self): # Beginning of the Game
		print('*** Lets Play Tic-Tac-Toe ***')
		self.display_grid()
		self.logic_obj.grid_contents = [' ']*9
		
		user_var, comp_var = self.user_comp_variable()
		
		while(self.game_end_status == 'continue'):
            # Accept User Position
			user_position = int(input(f'Enter Position to place \'{user_var}\' : '))
            # Update Positions in Grid
			self.logic_obj.move_count = self.logic_obj.update_grid((user_position, user_var), self.logic_obj.move_count)
			self.display_grid()
			
			self.game_end_status = self.logic_obj.win_lose()
			if self.game_end_status != 'continue':
				break
			
			comp_position = choice(self.logic_obj.rem_positions)
			
			print(f'Computer Plays \'{comp_var}\' at position {comp_position}')
			self.logic_obj.move_count = self.logic_obj.update_grid((comp_position, comp_var), self.logic_obj.move_count)
			self.display_grid()
			
			self.game_end_status = self.logic_obj.win_lose()
		
		self.display_result()

tic_tac_toe = game()
tic_tac_toe.start_game()