#Problem 11:find the greatest product of four adjacent numbers
#Vertically, horizontally, diagonally

grid = []
limit = 4
with open("problem_11_grid.txt",'r') as f:
    lines = [x.strip() for x in f.readlines()]
    for l in lines:
        grid.append([int(x) for x in l.split()])

#returns current if current is greater than max, max if otherwise
def f_setIfGreaterThan(currentVal,maxVal):
    if currentVal > maxVal:
        return currentVal
    else:
        return maxVal

def f_getMaxHorizontalProduct(this_grid):
    global limit
    max_horizontal_product = 0
    for line in this_grid:
        len_line = len(line)
        for x in range(len_line-limit+1):
            current_horizontal_product = line[x]
            for n in line[x+1:x+limit]:
                current_horizontal_product *= n
            if current_horizontal_product > max_horizontal_product:
                max_horizontal_product = current_horizontal_product
    return max_horizontal_product

def f_getMaxVerticalProduct(this_grid):
    global limit
    #first transform the grid
    vert_grid = [[0 for y in range(len(this_grid))] for x in range(len(this_grid))]
    len_grid = len(this_grid)
    for y in range(len_grid):
        for x in range(len_grid):
            vert_grid[x][y] = this_grid[y][x]
    return f_getMaxHorizontalProduct(vert_grid)

def f_getDiagonalProducts(this_grid):
    global limit
    right_offsets = []
    left_offsets = []
    for x in range(limit):
        right_offsets.append((x,x))
        left_offsets.append((x,limit-x-1))
    right_max = 0
    left_max = 0
    last_grid = len(this_grid) - limit + 1
    last_line = len(this_grid[0]) - limit + 1

    for y in range(last_grid):
        for x in range(last_line):
            current_right = 1
            for offset in right_offsets:
                current_right *= grid[y+offset[1]][x+offset[0]]
            right_max = f_setIfGreaterThan(current_right,right_max)

            current_left = 1
            for offset in left_offsets:
                current_left *= grid[y+offset[1]][x+offset[0]]
            left_max = f_setIfGreaterThan(current_left,left_max)
    return (left_max,right_max)




print("Horizontal:",f_getMaxHorizontalProduct(grid))
print("Vertical:",f_getMaxVerticalProduct(grid))
left_max, right_max = f_getDiagonalProducts(grid)
print("Diagonals: {}, {}".format(left_max,right_max))