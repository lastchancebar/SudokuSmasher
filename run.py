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

# This function finds an empty cell in the puzzle

def find_next_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i,j] == 0:
                row = i
                vol = j
                Fill_Chk = 1
                result = np.array([row,col,Fill_Chk], dtype="int8")
                return result
                result = np.array(-1,-1,0])
                return result
