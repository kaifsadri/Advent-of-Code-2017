from collections import deque
from itertools import islice
from functools import reduce

puz = "uugsqrei"


def knot(P):
    L = [ord(i) for i in P] + [
        17,
        31,
        73,
        47,
        23,
    ]
    skip = 0
    D = deque(range(256))
    r = 0
    for _ in range(64):
        for l in L:
            d = deque()
            for i in range(l):
                d.appendleft(D.popleft())
            D.extend(d)
            D.rotate(-skip)
            r += l + skip
            skip += 1
    D.rotate(r % 256)
    # Format the output
    result = ""
    for i in range(16):
        h = reduce(lambda x, y: x ^ y, islice(D, i * 16, (i + 1) * 16))
        result += bin(h)[2:].zfill(8)
    return result


disk = set()
for x in range(128):
    k = knot((puz + "-" + str(x)))
    for y, ch in enumerate(k):
        if ch == "1":
            disk.add((x, y))
print(f"Part 1: {len(disk)}")

groups = 0
while disk:
    g = {disk.pop()}
    while g:
        p = g.pop()
        adj = {
            (p[0] + d[0], p[1] + d[1])
            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if (p[0] + d[0], p[1] + d[1]) in disk
        }
        g = g.union(adj)
        disk -= adj
    groups += 1
print(f"Part 2: {groups}")
