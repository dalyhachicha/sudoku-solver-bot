
import numpy as np
import time

#Local import
from solver import isPossible
from output import Output

print("This bot will solve a sudoku game from [www.sudoku.com]")
# GLOBAL GRID VAR
grid = []

# User input Grid
while True:
    while True:
        row = list(input('Enter Row ['+str(len(grid))+']: '))
        if len(row) == 9:
            break
        else:
            print("Row length must be 9, Re-enter Row "+str(len(grid)))
            
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid) == 9:
        break
    print('Row ' + str(len(grid)) + ' Complete')

print('Please place your cursor on sudoku grid [0,0]')
time.sleep(2)
print('Started ...')

# Recursive solve
def main():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if isPossible(x, y, n,grid):
                        grid[y][x] = n
                        main()
                        grid[y][x] = 0
                return
    Output(grid)
    

main()
print('Solved <3')