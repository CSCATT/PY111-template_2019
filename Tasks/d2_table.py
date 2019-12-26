import numpy as np


N = 3
M = 4

i = 0
j = 0

steps [(0, 0)]

A = np.array([[2, 7, 9, 3],
              [12, 4, 1, 9],
              [1, 5, 2, 5]])

B[0, 0] = A[0, 0]
for i in range (1, N):
    A[1, 0] = A[i - 1, 0] + A[i, 0]

for j in range



def moove ():

    global tab
    tab = [2, 7, 9, 3, 12, 4, 1, 9, 1, 5, 2, 5]
    print("", tab[0: 4], "\n", tab[4: 8], "\n", tab[8: 12])

    step_check(0)


def step_check (point):
    ''' side check '''
    TOP = -4
    DOWN = 4
    LEFT = -1
    RIGHT = 1

    list_ = ()
    list_.append(tab[point+RIGHT])
    list_.append(tab[point+DOWN])

    print(list_)

    return min(list_)

moove()