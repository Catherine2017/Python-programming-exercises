# -*- coding:utf-8 -*-
def move(n, a, b, c):
    if n == 1:
        print(n, 'from', a, 'to', c)
    else:
        move(n-1, a, c, b)
        print(n, 'from', a, 'to', c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')
