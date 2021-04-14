P = open("11.txt").readline().strip().split(",")

# model hex grid with cube coordinations:
G = {
    "ne": (1, 0, -1),
    "n": (0, 1, -1),
    "nw": (-1, 1, 0),
    "sw": (-1, 0, 1),
    "s": (0, -1, 1),
    "se": (1, -1, 0),
}

s = [0, 0, 0]
M = 0
for move in P:
    s[0] += G[move][0]
    s[1] += G[move][1]
    s[2] += G[move][2]
    if (m := max(abs(s[0]), abs(s[1]), abs(s[2]))) > M:
        M = m
print(f"Part 1: {max(abs(s[0]), abs(s[1]), abs(s[2]))}")
print(f"Part 2: {M}")