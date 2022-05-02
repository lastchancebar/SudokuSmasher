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

# this function checks the validity og a number at a given position
#according to sudoku rules.

def check_input_validity(board,row,col,num):
    row_start=(row // 3) * 3
    col_start=(col // 3) * 3
    if num in board[:, col] or num in board[row,:]:
        return False
    if num in board[row_start:row_start + 3, col_start: + 3]:
        return False
    return True    

#generates an unsolved sudoku board based on required difficulty


def unsolved_puzzle(board, difficulty):
    count, done = 0, False
    if difficulty == "Easy":
        print("Generating Easy Puzzle...\n\n")
        upper_limit=35
    elif difficulty == "Medium":
        print("Generating puzzle of medium difficulty...\n\n")
        upper_limit=41 
    else: 
        print("Generating difficult puzzle...\n\n")
        upper_limit=47
    while True:
        i = random.randint(0,8)
        j = random.randint(0,8)  
        if count <=upper_limit:
            if board[i,j] != 0:
                not_check= board[i,j]
                board[i,j] = 0
                board_copy=board
                if solve_sudoku(board_copy, not_check):
                    board[i,j]= not_check
                    continue 
                row_start=(i // 3) * 3
                col_start=(j // 3) * 3
                if difficulty == "Easy":
                    if np.count_nonzero(board[row_start:row_start+3, col_start: col_start+3]) < 5:
                        board[i,j]=not_check
                        continue
                elif difficulty == "Medium":
                    if np.count_nonzero(board[row_start:row_start+3, col_start: col_start+3]) < 4:
                        board[i,j]=not_check
                        continue
                else:
                    if np.count_nonzero(board[row_start:row_start+3, col_start: col_start+3]) < 3:
                        board[i,j]=not_check
                count+=1
        else:
            done=True
            break        

