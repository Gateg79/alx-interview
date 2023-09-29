#!/usr/bin/python3
"""
Define island perimeter function that finds the perimeter
of an island in a body of water
"""

bdy_1 = set()
bdy_2 = set()
bdy_3 = set()
bdy_4 = set()


def edge(grid, i, j):
    """Find cells with either 1, 2, 3 or 4 exposed boundary and add them to
       appropriate set
       grid (list): 2d list
       i (int): row number
       j (int): column number
    """
    bdys = 0
    try:
        if i == 0:
            bdys += 1
        elif grid[i-1][j] == 0:
            bdys += 1
    except:
        bdys += 1
    try:
        if grid[i+1][j] == 0:
            bdys += 1
    except:
        bdys += 1
    try:
        if grid[i][j+1] == 0:
            bdys += 1
    except:
        bdys += 1
    try:
        if j == 0:
            bdys += 1
        elif grid[i][j-1] == 0:
            bdys += 1
    except:
        bdys += 1

    if bdys == 1:
        bdy_1.add((i, j))
    elif bdys == 2:
        bdy_2.add((i, j))
    elif bdys == 3:
        bdy_3.add((i, j))
    elif bdys == 4:
        bdy_4.add((i, j))


def island_perimeter(grid):
    """
    Calculate and return perimeter of island in the grid
    Grid is a rectangular grid where 0s represent water and 1s represent land
    Each cell is a square with a side length of 1
    There is only one island
    Grid is a 2D list of ints either 0 or 1
    Return perimeter of island
    """
    if grid == []:
        return 0
    l = len(grid)
    w = len(grid[0])
    for i in range(l):
        for j in range(w):
            if grid[i][j] == 1:
                edge(grid, i, j)
                if len(bdy_4) != 0:
                    return 4
    perimeter = (len(bdy_3) * 3) + (len(bdy_2) * 2) + (len(bdy_1))
    return perimeter
