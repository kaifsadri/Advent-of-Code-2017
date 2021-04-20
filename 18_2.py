from collections import defaultdict, deque

L = [line.strip().split() for line in open("18.txt").readlines()]
B = {0: deque(), 1: deque()}
W = {0: False, 1: False}
N = 0

R0 = defaultdict(int)
R0["p"] = 0
pos0 = 0
R1 = defaultdict(int)
R1["p"] = 1
pos1 = 0
while (pos1 < len(L) or pos0 < len(L)) and (not W[0] or not W[1]):
    if pos0 < len(L):
        l0 = L[pos0]
        if len(l0) == 3:
            try:
                v = int(l0[2])
            except ValueError:
                v = R0[l0[2]]
        if l0[0] == "set":
            R0[l0[1]] = v
            pos0 += 1
        elif l0[0] == "add":
            R0[l0[1]] += v
            pos0 += 1
        elif l0[0] == "mod":
            R0[l0[1]] %= v
            pos0 += 1
        elif l0[0] == "mul":
            R0[l0[1]] *= v
            pos0 += 1
        elif l0[0] == "snd":
            B[1].append(R0[l0[1]])
            pos0 += 1
        elif l0[0] == "jgz":
            try:
                o = int(l0[1])
            except ValueError:
                o = R0[l0[1]]
            if o > 0:
                pos0 += v
            else:
                pos0 += 1
        elif l0[0] == "rcv":
            try:
                R0[l0[1]] = B[0].popleft()
                W[0] = False
                pos0 += 1
            except IndexError:
                W[0] = True

    if pos1 < len(L):
        l1 = L[pos1]
        if len(l1) == 3:
            try:
                v = int(l1[2])
            except ValueError:
                v = R1[l1[2]]
        if l1[0] == "set":
            R1[l1[1]] = v
            pos1 += 1
        elif l1[0] == "add":
            R1[l1[1]] += v
            pos1 += 1
        elif l1[0] == "mod":
            R1[l1[1]] %= v
            pos1 += 1
        elif l1[0] == "mul":
            R1[l1[1]] *= v
            pos1 += 1
        elif l1[0] == "snd":
            B[0].append(R1[l1[1]])
            N += 1
            pos1 += 1
        elif l1[0] == "jgz":
            try:
                o = int(l1[1])
            except ValueError:
                o = R1[l1[1]]
            if o > 0:
                pos1 += v
            else:
                pos1 += 1
        elif l1[0] == "rcv":
            try:
                R1[l1[1]] = B[1].popleft()
                W[1] = False
                pos1 += 1
            except IndexError:
                W[1] = True

print(f"Part 2: {N}")