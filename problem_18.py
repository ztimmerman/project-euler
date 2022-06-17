#Problem 18, solve a triangle

#Build the triangle
triangle = []
with open("problem_18.txt",'r') as f:
    for l in f.readlines():
        triangle.append([int(x) for x in l.strip().split()])

#Calculate best route for triangle
top = 0
bottom = len(triangle)
current_level = bottom - 1
while current_level >= top:
    None