from collections import defaultdict

L = [line.strip().split() for line in open("18.txt").readlines()]

R = defaultdict(int)
pos = 0
Sound = 0
while pos < len(L):
    l = L[pos]
    if len(l) == 3:
        try:
            v = int(l[2])
        except ValueError:
            v = R[l[2]]
    if l[0] == "set":
        R[l[1]] = v
        pos += 1
    elif l[0] == "add":
        R[l[1]] += v
        pos += 1
    elif l[0] == "mod":
        R[l[1]] %= v
        pos += 1
    elif l[0] == "mul":
        R[l[1]] *= v
        pos += 1
    elif l[0] == "snd":
        Sound = R[l[1]]
        pos += 1
    elif l[0] == "jgz":
        try:
            o = int(l[1])
        except ValueError:
            o = R[l[1]]
        if o > 0:
            pos += v
        else:
            pos += 1
    elif l[0] == "rcv":
        if R[l[1]] != 0:
            print(f"Part 1: {Sound}")
            break
