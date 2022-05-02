import numpy as np
import random

#Prints sudoku array in familiar format


def Show_Board(board):
    for i in range(9): #i represents row
        for j in range(9): #j represents column
            if j == 0:
                print("|", end='')
            if j != 8:
                print(board[i,j], end ='')
            else:
                print(board[i,j], end='') 
            if (j+1) %  3 == 0:
                print("|", end='')
        if (i+1) %  3 == 0:
                print("\n--------------------", end='')
        print()                