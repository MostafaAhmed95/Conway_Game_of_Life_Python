import numpy as np


class Mop:
    """used to contain methods of differeent matmatical operations on list"""
    def __init__(self,length,width,span):
        self.length = length
        self.width = width
        self.span = span
        #print(self.length/self.span)
        self.l = np.zeros((int(self.length/self.span), int(self.width/self.span)))
        self.n_l = np.zeros((int(self.length / self.span), int(self.width / self.span)))
    def init_pos(self,row,column):
        """initialize squares of the game"""
        self.l[row][column] = 1

    def calc_alive(self,i, j):
        # upper left corner
        if i == 0 and j == 0:
            if self.l[i + 1][j] + self.l[i][j + 1] + self.l[i + 1][j + 1] == 2 or self.l[i + 1][j] + self.l[i][j + 1] + self.l[i + 1][j + 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0
        # lower right corner
        elif i == self.l.shape[0] - 1 and j == self.l.shape[1] - 1:
            if self.l[i][j - 1] + self.l[i - 1][j] + self.l[i - 1][j - 1] == 2 or self.l[i][j - 1] + self.l[i - 1][j] + self.l[i - 1][j - 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0
        # upper right corner
        elif i == 0 and j == self.l.shape[1] - 1:
            if self.l[i][j - 1] + self.l[i + 1][j] + self.l[i + 1][j - 1] == 2 or self.l[i][j - 1] + self.l[i + 1][j] + self.l[i + 1][j - 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0
        # lower left corner
        elif i == self.l.shape[0] - 1 and j == 0:
            if self.l[i - 1][j] + self.l[i][j + 1] + self.l[i - 1][j + 1] == 2 or self.l[i - 1][j] + self.l[i][j + 1] + self.l[i - 1][j + 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0
        # first row
        elif i == 0:
            if self.l[i][j - 1] + self.l[i][j + 1] + self.l[i + 1][j - 1] + self.l[i + 1][j] + self.l[i + 1][j + 1] == 2 or self.l[i][j - 1] + \
                    self.l[i][j + 1] + self.l[i + 1][j - 1] + self.l[i + 1][j] + self.l[i + 1][j + 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0
        # last row
        elif i == self.l.shape[0] - 1:
            if self.l[i][j - 1] + self.l[i][j + 1] + self.l[i - 1][j - 1] + self.l[i - 1][j] + self.l[i - 1][j + 1] == 2 or self.l[i][j - 1] + \
                    self.l[i][j + 1] + self.l[i - 1][j - 1] + self.l[i - 1][j] + self.l[i - 1][j + 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0
        # first col
        elif j == 0:
            if self.l[i - 1][j] + self.l[i + 1][j] + self.l[i - 1][j + 1] + self.l[i][j + 1] + self.l[i + 1][j + 1] == 2 or self.l[i - 1][j] + \
                    self.l[i + 1][j] + self.l[i - 1][j + 1] + self.l[i][j + 1] + self.l[i + 1][j + 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0
        # last col
        elif j == self.l.shape[1] - 1:
            if self.l[i + 1][j] + self.l[i - 1][j] + self.l[i - 1][j - 1] + self.l[i][j - 1] + self.l[i + 1][j - 1] == 2 or self.l[i + 1][j] + \
                    self.l[i - 1][j] + self.l[i - 1][j - 1] + self.l[i][j - 1] + self.l[i + 1][j - 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0
        # all normal squares
        else:
            if self.l[i - 1][j - 1] + self.l[i - 1][j] + self.l[i - 1][j + 1] + self.l[i][j + 1] + self.l[i + 1][j + 1] + self.l[i + 1][j] + \
                    self.l[i + 1][j - 1] + self.l[i][j - 1] == 2 or self.l[i - 1][j - 1] + self.l[i - 1][j] + self.l[i - 1][j + 1] + self.l[i][
                j + 1] + self.l[i + 1][j + 1] + self.l[i + 1][j] + self.l[i + 1][j - 1] + self.l[i][j - 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0

    def calc_dead(self,i, j):
        # upper left corner
        # print("hola")
        if i == 0 and j == 0:
            if self.l[i + 1][j] + self.l[i][j + 1] + self.l[i + 1][j + 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0
        # lower right corner
        elif i == self.l.shape[0] - 1 and j == self.l.shape[1] - 1:
            if self.l[i][j - 1] + self.l[i - 1][j] + self.l[i - 1][j - 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0
        # upper right corner
        elif i == 0 and j == self.l.shape[1] - 1:
            if self.l[i][j - 1] + self.l[i + 1][j] + self.l[i + 1][j - 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0
        # lower left corner
        elif i == self.l.shape[0] - 1 and j == 0:
            if self.l[i - 1][j] + self.l[i][j + 1] + self.l[i - 1][j + 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0

        # first row
        elif i == 0:
            if self.l[i][j - 1] + self.l[i][j + 1] + self.l[i + 1][j - 1] + self.l[i + 1][j] + self.l[i + 1][j + 1] == 3:
                self.n_l[i][j] = 1
            else:
                #print(i, j)
                self.n_l[i][j] = 0
        # last row
        elif i == self.l.shape[0] - 1:
            if self.l[i][j - 1] + self.l[i][j + 1] + self.l[i - 1][j - 1] + self.l[i - 1][j] + self.l[i - 1][j + 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0
        # first col
        elif j == 0:
            if self.l[i - 1][j] + self.l[i + 1][j] + self.l[i - 1][j + 1] + self.l[i][j + 1] + self.l[i + 1][j + 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0
        # last col
        elif j == self.l.shape[1] - 1:
            if self.l[i + 1][j] + self.l[i - 1][j] + self.l[i - 1][j - 1] + self.l[i][j - 1] + self.l[i + 1][j - 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0
        # all normal squares
        else:
            if self.l[i - 1][j - 1] + self.l[i - 1][j] + self.l[i - 1][j + 1] + self.l[i][j + 1] + self.l[i + 1][j + 1] + self.l[i + 1][j] + \
                    self.l[i + 1][j - 1] + self.l[i][j - 1] == 3:
                self.n_l[i][j] = 1
            else:
                self.n_l[i][j] = 0

    def next_it(self):
        """give me the shape of next iteration"""
        self.n_l = np.zeros((15, 15))
        for i in range(self.l.shape[0]):
            for j in range(self.l.shape[1]):
                #print(i,j)
                if self.l[i][j] == 1:
                    self.calc_alive(i, j)
                else:
                    self.calc_dead(i, j)
        self.l=self.n_l




