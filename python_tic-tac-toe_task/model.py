"""module, contains tictactoe model"""


class Model:
    """class, contains model"""
    def __init__(self):
        self.cells = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def get(self, xy_coords):
        """coordinates getter"""
        x_coord, y_coord = xy_coords
        if 0 <= x_coord < 3 and 0 <= y_coord < 3:
            return self.cells[x_coord][y_coord]

    def set(self, xy_coords, val):
        """xy is tuple of coordinates which will be filled with val"""
        x_coord, y_coord = xy_coords
        if (self.cells[x_coord][y_coord] == 0) and 1 <= val <= 2:
            self.cells[x_coord][y_coord] = val

    def get_row(self, number):
        """returns specified row"""
        if 0 <= number < 3:
            return [self.cells[number][i] for i in range(3)]
        return None

    def get_column(self, number):
        """returns specified column"""
        if 0 <= number < 3:
            return [self.cells[i][number] for i in range(3)]
        return None

    def get_diagonal(self, number):
        """returns main diagonal for n=0 and other for n=1"""
        if number == 0:   # pylint has a BIIIIG fuckup here
            return [self.cells[i][i] for i in range(3)]
        elif number == 1:
            return [self.cells[i][2 - i] for i in range(3)]
        else:
            return None

    def check_win(self):
        """checking all lines"""
        for i in range(3):  # checking cols and rows
            row = self.get_row(i)
            if row[0] == row[1] == row[2]:
                return row[0]
            col = self.get_column(i)
            if col[0] == col[1] == col[2]:
                return col[0]

        for i in range(2):  # checking diagonals
            diag = self.get_diagonal(i)
            if diag[0] == diag[1] == diag[2]:
                return diag[0]

        count = 0  # counting x-es and o-s
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] != 0:
                    count += 1
        if count == 9:  # draw
            return 3
        return 0  # in the middle of game
