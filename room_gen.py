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
            room_array[i][j] = WALL if i == 0 or j == 0 or i == y - \
                1 or j == x - 1 else FLOOR
    return room_array


# Take a size 'x' & 'y'
# Return an array of char shaped like an ellipse
# /!\ w: total width of the shape (x)
# /!\ h: total height of the shape (y)
# if any of those value is even it'll be rounded to the next odd value
#   ex : 4 become 5 & 2 become 3
def get_RoundRoom(w, h):
    yc = w // 2
    xc = h // 2
    if yc < 1 or xc < 1:
        return [0]
    sy = (2 * yc) + 1
    sx = (2 * xc) + 1
    width = xc
    height = yc
    room_array = [[0] * sy for i in range(sx)]
    a2 = width * width
    b2 = height * height
    fa2 = 4 * a2
    fb2 = 4 * b2

    # first half
    x = 0
    y = height
    sigma = 2 * b2 + a2 * (1 - 2 * height)
    while b2 * x <= a2 * y:
        room_array[xc + x][yc + y] = WALL
        room_array[xc - x][yc + y] = WALL
        room_array[xc + x][yc - y] = WALL
        room_array[xc - x][yc - y] = WALL
        if sigma >= 0:
            sigma += fa2 * (1 - y)
            y -= 1
        sigma += b2 * ((4 * x) + 6)
        x += 1

    # second half
    x = width
    y = 0
    sigma = 2 * a2 + b2 * (1 - 2 * width)
    while a2 * y <= b2 * x:
        room_array[xc + x][yc + y] = WALL
        room_array[xc - x][yc + y] = WALL
        room_array[xc + x][yc - y] = WALL
        room_array[xc - x][yc - y] = WALL
        if sigma >= 0:
            sigma += fb2 * (1 - x)
            x -= 1
        sigma += a2 * ((4 * y) + 6)
        y += 1
    return room_array


# # TEST PURPOSE
# import sys


# def writch(a):
#     # write char
#     sys.stdout.write(a)
#     sys.stdout.flush()


# # ra = get_RoundRoom2(5, 5)
# # ra = get_SquareRoom(10, 30)
# ra = get_RoundRoom(8, 6) #pos x
# for i in range(len(ra)):
#         writch('\n')
#         for j in range(len(ra[i])):
#             if ra[i][j] == ' ':
# #                print(ra[i][j])
#                 writch('X')
#             elif ra[i][j] == '#':
#                 writch('#')
#             else:
#                 writch('!')
