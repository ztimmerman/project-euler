#Problem 15
#Find how many routes there are for a 20x20 grid

routes = {(0,0):1}

def f_getRoutes(x,y):
    global routes
    if x == 0 or y == 0:
        return 1
    if (x,y) in routes:
        num_routes = routes[(x,y)]
        #print("{} found: {}".format((x,y),num_routes))
    else:
        #print((x,y))
        num_routes = f_getRoutes(x-1,y)+f_getRoutes(x,y-1)
        routes[(x,y)] = num_routes
    return num_routes

print(f_getRoutes(20,20))