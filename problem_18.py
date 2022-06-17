#Problem 18, solve a triangle

#Build the triangle
triangle = []
with open("problem_18.txt",'r') as f:
    for l in f.readlines():
        triangle.append([int(x) for x in l.strip().split()])

#Calculate best route for triangle
top = 0
bottom = len(triangle) - 1
current_level = bottom - 1
while current_level >= top:
    lower_level = current_level + 1
    for x in range(len(triangle[current_level])):
        a = triangle[lower_level][x]
        b = triangle[lower_level][x+1]
        if a >= b:
            triangle[current_level][x]+=a
        else:
            triangle[current_level][x]+=b
    #go up a level
    current_level -= 1

print(triangle[0])