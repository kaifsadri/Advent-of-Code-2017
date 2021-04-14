L = [line.strip() for line in open("12.txt").readlines()]
P = dict()
for l in L:
    p = l.split(" <-> ")
    P[int(p[0])] = list(map(lambda x: int(x), p[1].split(", ")))


def group(prog, P):
    togo = {prog}
    been = set()
    while togo:
        p = togo.pop()
        been.add(p)
        for other in P[p]:
            if other not in been:
                togo.add(other)
    return frozenset(been)


print(f"Part 1: {len(group(0, P))}")

G = set(group(p, P) for p in P)
print(f"Part 2: {len(G)}")
