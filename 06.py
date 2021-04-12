# Puzzle input
D = list(map(lambda x: int(x), "0 5 10 0 11 14 13 4 11 8 8 7 1 4 12 11".split()))
H = set()
conf = tuple(D)
N = 0
while conf not in H:
    H.add(conf)
    N += 1
    im, mx = 0, D[0]
    for j in enumerate(D):
        if j[1] > mx:
            im, mx = j[0], j[1]
    D[im] = 0
    im += 1
    while mx:
        D[im % len(D)] += 1
        im += 1
        mx -= 1
    conf = tuple(D)
print(f"Part 1: {N}")

# re-run with the new state as starting conf
H = set()
conf = tuple(D)
N = 0
while conf not in H:
    H.add(conf)
    N += 1
    im, mx = 0, D[0]
    for j in enumerate(D):
        if j[1] > mx:
            im, mx = j[0], j[1]
    D[im] = 0
    im += 1
    while mx:
        D[im % len(D)] += 1
        im += 1
        mx -= 1
    conf = tuple(D)
print(f"Part 2: {N}")