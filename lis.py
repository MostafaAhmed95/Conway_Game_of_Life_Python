import numpy as np


class Mop:
    """Used to contain methods of differeent matmatical operations on list"""
    def __init__(self, length, width, span):
        self.length = length
        self.width = width
        self.span = span
        self.l = np.zeros((int(self.length/self.span), int(self.width/self.span)))
        self.n_l = np.zeros((int(self.length / self.span), int(self.width / self.span)))

    def init_pos(self, row, column):
        """initialize squares of the game"""
        self.l[row][column] = 1

    def alive(self,r,c):
        alive_cells=0
        #the cell is alive or not
        if self.l[r][c]==1:
            alive_cells=-1
        for i in range(r - 1, (r - 1) + 3):
            for j in range(c - 1, (c - 1) + 3):
                if i in range(self.l.shape[0]) and j in range(self.l.shape[1]):
                    if self.l[i][j] == 1:
                        alive_cells = alive_cells + 1

        #conditions of living
        if self.l[r][c] == 0 and alive_cells == 3:
            self.n_l[r][c] = 1
        elif self.l[r][c] == 1 and 2 <= alive_cells <=3:
            self.n_l[r][c] = 1
        else:
            self.n_l[r][c] = 0
    def next_it(self):
        """give me the shape of next iteration"""
        self.n_l = np.zeros((15, 15))
        for i in range(self.l.shape[0]):
            for j in range(self.l.shape[1]):
                self.alive(i,j)
                '''
                if self.l[i][j] == 1:
                    self.calc_alive(i, j)
                else:
                    self.calc_dead(i, j)
                '''
        self.l=self.n_l




