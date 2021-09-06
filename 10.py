from collections import deque
from itertools import islice
from functools import reduce

# Part 1:
P = "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216"

L = [int(i) for i in P.split(",")]

D = deque(range(256))
r = 0  # number of rotations performed
for skip, l in enumerate(L):
    d = deque()
    for i in range(l):
        d.appendleft(D.popleft())
    D.extend(d)
    D.rotate(-skip)
    r += l + skip
    # print(D)
D.rotate(r % 256)
print(f"Part 1: {D[0] * D[1]}")

# Part 2:
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
print("Part 2: ", end="")
for i in range(16):
    h = reduce(lambda x, y: x ^ y, islice(D, i * 16, (i + 1) * 16))
    print(hex(h)[2:].zfill(2), end="")
print()
