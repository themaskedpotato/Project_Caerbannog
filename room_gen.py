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
            room_array[i][j] = '#' if i == 0 or j == 0 or i == y-1 or j == x-1 else ' '
    return room_array