L = [line.strip() for line in open("20.txt").readlines()]
D = dict()
for i, l in enumerate(L):
    t = l.split(", ")
    exec("p=(" + t[0][3:-1] + ")")
    exec("v=(" + t[1][3:-1] + ")")
    exec("a=(" + t[2][3:-1] + ")")
    exec("D[i] = (p, v, a)")

# the particle that eventually stays closest is the one that has the minimum absolute acceleration
# If there are many, the one closest to the sun to begin with, will be the closest eventually
m = min(D.values(), key=lambda x: abs(x[2][0]) + abs(x[2][1]) + abs(x[2][2]))
m = abs(m[2][0]) + abs(m[2][1]) + abs(m[2][2])
print(
    "Part 1: ",
    min(
        [x for x in D if abs(D[x][2][0]) + abs(D[x][2][1]) + abs(D[x][2][2]) == m],
        key=lambda x: abs(D[x][0][0]) + abs(D[x][0][1]) + abs(D[x][0][2]),
    ),
)

# part 2:
# movement of particles quickly diverges
# so about 2,000 runs is more than sufficient to find the answer
M = 1000
for i in range(2_000):
    # update accel and pos:
    P = list()
    for s in D:
        v = (
            D[s][1][0] + D[s][2][0],
            D[s][1][1] + D[s][2][1],
            D[s][1][2] + D[s][2][2],
        )
        p = (
            D[s][0][0] + v[0],
            D[s][0][1] + v[1],
            D[s][0][2] + v[2],
        )
        D[s] = (p, v, D[s][2])
        P.append(p)
    # now filter collisions:
    R = set()
    for s in D:
        if P.count(D[s][0]) > 1:
            R.add(s)
    for r in R:
        del D[r]
    if len(D) < M:
        M = len(D)
print(f"Part 2: {M}")
