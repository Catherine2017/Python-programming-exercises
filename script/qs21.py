import math


def root_move():
    pos = [0, 0]
    while True:
        s = input()
        if s == "STOP":
            break
        item = s.split(" ")
        val = int(item[1])
        if item[0] == "LEFT":
            pos[0] -= val
        elif item[0] == "RIGHT":
            pos[0] += val
        elif item[0] == "UP":
            pos[1] += val
        elif item[0] == "DOWN":
            pos[1] -= val
        else:
            pass
    return int(math.sqrt(pos[0]**2+pos[1]**2))


print(root_move())
