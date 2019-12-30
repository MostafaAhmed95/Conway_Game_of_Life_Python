import numpy as np
l = np.zeros((5,5))
l[1][1]=1
l[1][2]=1
l[1][3]=1
#print(l)
n_l = np.zeros((5,5))


def calc_alive(i,j):
    #upper left corner
    if i==0 and j==0:
        if l[i+1][j] + l[i][j+1] + l[i+1][j+1] == 2 or l[i+1][j] + l[i][j+1] + l[i+1][j+1] == 3 :
            n_l[i][j]=1
        else:
            n_l[i][j]=0
    #lower right corner
    elif i==l.shape[0]-1 and j==l.shape[1]-1:
        if l[i][j-1] + l[i-1][j] + l[i-1][j-1] == 2 or l[i][j-1] + l[i-1][j] + l[i-1][j-1] == 3 :
            n_l[i][j]=1
        else:
            n_l[i][j]=0
    #upper right corner
    elif i==0 and j == l.shape[1]-1:
        if l[i][j-1] + l[i+1][j] + l[i+1][j-1] == 2 or l[i][j-1] + l[i+1][j] + l[i+1][j-1] == 3 :
            n_l[i][j]=1
        else:
            n_l[i][j]=0
    # lower left corner
    elif i == l.shape[0]-1 and j == 0:
        if l[i-1][j] + l[i][j+1] + l[i-1][j+1] == 2 or l[i-1][j] + l[i][j+1] + l[i-1][j+1] == 3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0
    #first row
    elif i == 0:
        if l[i][j-1] + l[i][j+1] + l[i+1][j-1] + l[i+1][j] + l[i+1][j+1] == 2 or l[i][j-1] + l[i][j+1] + l[i+1][j-1] + l[i+1][j] + l[i+1][j+1] == 3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0
    # last row
    elif i == l.shape[0]-1:
        if l[i][j-1] + l[i][j+1] + l[i-1][j-1] + l[i-1][j] + l[i-1][j+1] == 2 or l[i][j-1] + l[i][j+1] + l[i-1][j-1] + l[i-1][j] + l[i-1][j+1] == 3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0
    #first col
    elif j == 0:
        if l[i-1][j] + l[i+1][j] + l[i-1][j+1] + l[i][j+1] + l[i+1][j+1] ==2 or l[i-1][j] + l[i+1][j] + l[i-1][j+1] + l[i][j+1] + l[i+1][j+1] == 3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0
    # last col
    elif j == l.shape[1]-1:
        if l[i+1][j] + l[i-1][j] + l[i-1][j-1] + l[i][j-1] + l[i+1][j-1]==2 or l[i+1][j] + l[i-1][j] + l[i-1][j-1] + l[i][j-1] + l[i+1][j-1]==3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0
    #all normal squares
    else:
        if l[i-1][j-1] + l[i-1][j] + l[i-1][j+1] + l[i][j+1] + l[i+1][j+1] + l[i+1][j] + l[i+1][j-1] + l[i][j-1]== 2 or l[i-1][j-1] + l[i-1][j] + l[i-1][j+1] + l[i][j+1] + l[i+1][j+1] + l[i+1][j] + l[i+1][j-1] + l[i][j-1]== 3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0
def calc_dead(i,j):
    # upper left corner
    #print("hola")
    if i == 0 and j == 0:
        if l[i + 1][j] + l[i][j + 1] + l[i + 1][j + 1] == 3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0
    # lower right corner
    elif i == l.shape[0]-1 and j == l.shape[1]-1:
        if l[i][j - 1] + l[i - 1][j] + l[i - 1][j - 1] == 3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0
    # upper right corner
    elif i == 0 and j == l.shape[1]-1:
        if l[i][j - 1] + l[i + 1][j] + l[i + 1][j - 1] == 3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0
    # lower left corner
    elif i == l.shape[0]-1 and j == 0:
        if l[i - 1][j] + l[i][j + 1] + l[i - 1][j + 1] == 3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0

    # first row
    elif i == 0:
        if l[i][j-1] + l[i][j+1] + l[i+1][j- 1] + l[i + 1][j] + l[i + 1][j + 1] == 3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0
    # last row
    elif i == l.shape[0]-1:
        if l[i][j - 1] + l[i][j + 1] + l[i - 1][j - 1] + l[i - 1][j] + l[i - 1][j + 1] == 3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0
    # first col
    elif j == 0:
        if l[i - 1][j] + l[i + 1][j] + l[i - 1][j + 1] + l[i][j + 1] + l[i + 1][j + 1] == 3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0
    # last col
    elif j == l.shape[1]-1:
        if l[i + 1][j] + l[i - 1][j] + l[i - 1][j - 1] + l[i][j - 1] + l[i + 1][j - 1] == 3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0
    # all normal squares
    else:
        if l[i-1][j-1] + l[i-1][j] + l[i-1][j+1] + l[i][j+1] + l[i+1][j+1] + l[i+1][j] + l[i+1][j-1] + l[i][j-1] == 3:
            n_l[i][j] = 1
        else:
            n_l[i][j] = 0


for i in range(l.shape[0]):
    for j in range(l.shape[1]):
       if l[i][j]==1:
           calc_alive(i,j)
       else:
           calc_dead(i,j)
