from collections import defaultdict

L = [line.strip().split() for line in open("23.txt").readlines()]
R = defaultdict(int)
pos = 0
N = 0
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
    elif l[0] == "sub":
        R[l[1]] -= v
        pos += 1
    elif l[0] == "mul":
        R[l[1]] *= v
        pos += 1
        N += 1
    elif l[0] == "jnz":
        try:
            o = int(l[1])
        except ValueError:
            o = R[l[1]]
        if o != 0:
            pos += v
        else:
            pos += 1

print(f"Part 1: {N}")

h = 0
for n in range(109900, 126900 + 1, 17):
    for i in range(2, n):
        if n % i == 0:
            h += 1
            break
print(f"Part 2: {h}")
