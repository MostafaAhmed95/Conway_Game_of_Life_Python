from tkinter import *
class Vis:
    """class for GUI"""
    def __init__(self,length,width,span):
        self.length = length
        self.width = width
        self.span = span
        self.top=Tk()
        self.top.geometry(str(length)+'x'+str(width))
        self.c = Canvas(self.top, height=300, width=300)
        for i in range(0, 300, 20):
            self.c.create_line(i, 0, i, 300, width=3)
            self.c.create_line(0, i, 300, i, width=3)
        self.c.pack()

    def colorize(self,l):
        """colorizing the squares"""
        self.c.delete('all')
        for i in range(0, 300, 20):
            self.c.create_line(i, 0, i, 300, width=3)
            self.c.create_line(0, i, 300, i, width=3)
        self.c.pack()
        for i in range(l.shape[0]):
            for j in range(l.shape[1]):
                if l[i][j] == 1:
                    self.c.create_rectangle(j * self.span, i * self.span,
                                            (j + 1) * self.span, (i + 1) * self.span, fill='red')
                    self.c.pack()