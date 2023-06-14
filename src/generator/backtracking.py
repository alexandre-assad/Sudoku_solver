from src.layout.game import *

def backtracking(grid):
    array_potential = []
    while grid.not_win():
        
        for i in range(9):
            for j in range(9):
                
                if grid.g_matrix[i][j].value == "_":
                    
                    for number in range(1,10):
                        if grid.is_case_numbered(i,j,number):
                            array_potential.append(number)

                    if grid.g_matrix[i][j].get_value(array_potential):
                        i = 0
                        j = 0
                    array_potential = []
                            
                            
    return grid