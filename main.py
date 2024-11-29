import math

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def computePointC(x_a, y_a, x_b):
    x_c = (x_b + x_a) / 2
    y_c = math.sqrt(math.pow(x_b - x_a, 2) - math.pow((x_b - x_a) / 2, 2)) + y_a

    return x_c, y_c


def chooseRandomCorner():
    rand = np.random.default_rng().random()

    if rand < 1 / 3:
        return "A"
    elif 1 / 3 <= rand < 2 / 3:
        return "B"
    else:
        return "C"


def computeNewPoint(corner, x, y, x_a, y_a, x_b, y_b, x_c, y_c):
    if corner == "A":
        newX = (x + x_a) / 2
        newY = (y + y_a) / 2
    elif corner == "B":
        newX = (x + x_b) / 2
        newY = (y + y_b) / 2
    else:
        newX = (x + x_c) / 2
        newY = (y + y_c) / 2

    return newX, newY


def computeTriangleSideEquations(x_a, y_a, x_b, y_b):
    x_c, y_c = computePointC(x_a, y_a, x_b)

    s_1 = (y_c - y_a) / (x_c - x_a)
    s_2 = (y_b - y_c) / (x_b - x_c)

    b_1 = y_c - s_1 * x_c
    b_2 = y_c - s_2 * x_c

    return s_1, b_1, s_2, b_2, y_c


def generateTriangleCoordinates(x_a, y_a, x_b, y_b):
    # get equation constants
    s_1, b_1, s_2, b_2, y_c = computeTriangleSideEquations(x_a, y_a, x_b, y_b)

    # generate random values
    u_x = np.random.default_rng().random()
    u_y = np.random.default_rng().random()

    # transform x and y values
    x_1 = x_a + (x_b - x_a) * u_x
    y_2 = y_a + (y_c - y_a) * u_y

    print(f'u_x: {u_x}, u_y: {u_y}, x_1: {x_1}, y_2: {y_2}')

    # compute y-values
    if x_a <= x_1 < (x_a + x_b) / 2:
        y_1 = s_1 * x_1 + b_1

        if y_2 <= y_1:
            print("Accept")
            return x_1, y_2
        else:
            print("Reject")
            return None, None

    elif (x_a + x_b) / 2 <= x_1 <= x_b:
        y_1 = s_2 * x_1 + b_2

        if y_2 <= y_1:
            print("Accept")
            return x_1, y_2
        else:
            print("Reject")
            return None, None
    else:
        print("ERROR: Faulty x-values!")


def getInitialCoordinates(x_a, y_a, x_b, y_b):
    initialX = None
    while initialX == None:
        initialX, initialY = generateTriangleCoordinates(x_a, y_a, x_b, y_b)

    return initialX, initialY


def generateSierpinskiPoints(num_of_points, triangle_left=(2,2), size=4):
    ## Initialize
    iter=0
    x_vec, y_vec = [], []

    # Check if first iteration
    if iter == 0:
        ## Triangle coordinates
        # point A
        x_a, y_a = triangle_left
        # point B
        x_b, y_b = x_a+size, y_a
        # point C
        x_c, y_c = computePointC(x_a, x_a, x_b)

        # collect in vector
        triangle_x = [x_a, x_b, x_c, x_a]
        triangle_y = [y_a, y_b, y_c, y_a]

        ## First random coordinate
        newX, newY = getInitialCoordinates(x_a, y_a, x_b, y_b)

    while iter < num_of_points:
        corner = chooseRandomCorner()
        newX, newY = computeNewPoint(corner, newX, newY, x_a, y_a, x_b, y_b, x_c, y_c)
        x_vec.append(newX)
        y_vec.append(newY)
        iter += 1

    return x_vec, y_vec, triangle_x, triangle_y



def update(i, triangle_x, triangle_y, x_vec, y_vec, speed_multiplier=1):
    i += 1
    image1.set_data(triangle_x, triangle_y)
    image2.set_data(x_vec[:i*speed_multiplier], y_vec[:i*speed_multiplier])

## Settings
no_of_points = 10000
speed_Multiplier = 100
X_vec, Y_vec, triangle_X, triangle_Y = generateSierpinskiPoints(no_of_points)

## Plotting
fig, ax = plt.subplots(figsize=(10,10))
image1, = ax.plot(triangle_X, triangle_Y)
image2, = ax.plot(X_vec, Y_vec, "o", markersize = 1)

## Animating
ani = animation.FuncAnimation(fig,
                              func=update,
                              fargs=[triangle_X, triangle_Y, X_vec, Y_vec, speed_Multiplier],
                              interval=1,
                              frames=int(no_of_points/speed_Multiplier),
                              repeat=False)
ani.save(f'triangle_animation_{speed_Multiplier}x_{no_of_points}N.gif', writer='imagemagick', fps=60)




# ax.plot(x_vec, y_vec, "bo", markersize=0.5)
# plt.show()

# i = 0
# x_vec = []
# y_vec = []
# while i < 10000:
#     # Setting triangle variables
#     print(i)
#     # point A
#     x_a = 2
#     y_a = 2
#
#     # point B
#     x_b = 6
#     y_b = y_a # redundant
#
#     x,y = generateTriangleCoordinates(x_a, y_a, x_b)
#
#     x_vec.append(x)
#     y_vec.append(y)
#     #print(f'X: {x}, Y: {y}')
#
#     i = i+1
#
# fig, ax = plt.subplots(figsize=(20, 20))
#
# ax.plot(x_vec, y_vec, "bo")
# plt.show()



