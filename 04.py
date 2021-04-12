L = [line.strip() for line in open("04.txt").readlines()]

M = 0
N = 0
for line in L:
    t = line.split()
    if sum([line.count(word) for word in t]) == len(t):
        M += 1
    t = [sorted(i) for i in t]
    if sum([t.count(word) for word in t]) == len(t):
        N += 1
print("Part 1: ", M)
print("Part 2: ", N)
