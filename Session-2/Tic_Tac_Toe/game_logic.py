class game_logic:

    def __init__(self):
        self.grid_contents = [x for x in range(9)]
        self.rem_positions = [x for x in range(9)]
        self.winner = ''
        self.move_count = 0

    def check_status(self, move_count):
        if move_count > 4:
            game_end_status = self.win_lose()
    
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

    def update_grid(self, position_tuple, move_count):
        self.fill_position(*position_tuple)
        return move_count + 1