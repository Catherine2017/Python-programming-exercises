import sys
tot = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    opr = values[0]
    num = int(values[1])
    if opr == "D":
        tot += num
    elif opr == 'W':
        tot -= num
    else:
        sys.stderr.write("Can not identify pattern!")
print(tot)
