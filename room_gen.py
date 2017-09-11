from constants import *
import math

# Take a size as 'x' and 'y'
# Return an array of char
# ex :
#    (x: 7  y: 4)
#       #######
#       #     #
#       #     #
#       #######


def get_SquareRoom(x, y):
    # Generator to create an empty square
    room_array = [[' '] * x for i in range(y)]
    # Create the external wall
    for i in range(len(room_array)):
        for j in range(len(room_array[i])):
            # a if cond else b
            room_array[i][j] = WALL if i == 0 or j == 0 or i == y-1 or j == x-1 else FLOOR
    return room_array


# Take a size 'x' & 'y'
# Return an array of char shaped like an ellipse
# ex :
# !
def get_RoundRoom(x, y):
    room_array = [[0] * x for i in range(y)]
    theta = 0 # Angle/incrementator for the circle (end when reaching 360)
    h, k = x / 2, y / 2 # coordination of the center of the room
    step = 10
    r = x / 2 if x > y else y / 2

    while theta <= 360: # Until for circle revolution
        n = h + r * math.cos(theta)
        m = k + r * math.sin(theta)
        # draw
        print("theta : ", theta)
        print("m : ", m)
        print("n : ", n)
        theta += step
    return room_array
