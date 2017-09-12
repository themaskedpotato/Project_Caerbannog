from constants import *

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

    # fill the fllor inside the ellipse
    room_array = floor_filling(room_array)
    return room_array


def find_NextItem(map_line, x_pos, item):
    # 'line' of the map to parse
    # 'position' in the line to start research
    # 'item' to look for
    y = 0
    x = x_pos + 1
    x = x_pos + 1 if x_pos + 1 < len(map_line) else x_pos
    while x < len(map_line):  # parse the line
        if map_line[x] != item:
            y += 1  # increment y if the item isn't found
        else:
            return y  # return the distance to item from x_pos if any
        x += 1
    return 0  # return 0 if no item has been found


def floor_filling(map_array):
    for i in range(len(map_array)):
        for j in range(len(map_array[i])):
            if map_array[i][j] == WALL:
                ln = find_NextItem(map_array[i], j, WALL)
                if ln:
                    k = j
                    while j < k + ln:
                        map_array[i][j + 1] = FLOOR
                        j += 1
    return map_array


# TEST PURPOSE
import sys


def writch(a):
    # write char
    sys.stdout.write(a)
    sys.stdout.flush()

def get_room_size(map_array):
    x_size = 0
    y_size = 0
    for i in range(len(map_array)):
        x_size += 32
        for j in range(len(map_array[i])):
            y_size += 32
    return (x_size, y_size)

# ra = get_RoundRoom2(5, 5)
# ra = get_SquareRoom(10, 30)
ra = get_RoundRoom(15, 20) #pos x
ra = floor_filling(ra)
for i in range(len(ra)):
        writch('\n')
        for j in range(len(ra[i])):
            if ra[i][j] == 'X':
#                print(ra[i][j])
                writch('X')
            elif ra[i][j] == '#':
                writch('#')
            else:
                writch('!')
# test = [20, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ret = find_NextItem(test, 0, 20)
# print(ret, len(test))


