from collections import defaultdict

P = [line.strip() for line in open("22.txt").readlines()]  # puzzle input
Gr = defaultdict(lambda: "0")
# centralize the grid
for row in range(len(P)):
    for col in range(len(P)):
        Gr[(col - len(P) // 2, -row + len(P) // 2)] = "1" if P[row][col] == "#" else "0"
# turns
R = {(1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0)}
L = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}

# part 1:
d = (0, 1)
l = (0, 0)
i = 0
N = 0
G = Gr.copy()
while i < 10_000:
    if G[l] == "0":  # if clean
        d = L[d]  # turn left
        N += 1  # count infections
    else:  # if infected
        d = R[d]  # turn right
    G[l] = "1" if G[l] == "0" else "0"
    l = (l[0] + d[0], l[1] + d[1])  # move
    i += 1
print(f"Part 1: {N}")

# part 2:
G = Gr.copy()
M = {"0": "w", "w": "1", "1": "f", "f": "0"}
d = (0, 1)
l = (0, 0)
i = 0
N = 0
while i < 10_000_000:
    # turn
    if G[l] == "0":  # if clean
        d = L[d]  # turn left
    elif G[l] == "1":  # if infected
        d = R[d]  # turn right
    elif G[l] == "f":
        d = (-d[0], -d[1])  # reverse
    elif G[l] == "w":
        pass  # no change in direction
    if M[G[l]] == "1":
        N += 1
    G[l] = M[G[l]]
    l = (l[0] + d[0], l[1] + d[1])  # move
    i += 1
print(f"Part 2: {N}")