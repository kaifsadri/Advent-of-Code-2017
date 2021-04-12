"""
17  16  15  14  13  .
18   5   4   3  12  .
19   6   1   2  11  28
20   7   8   9  10  27
21  22  23  24  25  26

The bottom right corner of each square is n**2 (n odd)
so n**2 is located at (n//2, n//2) if 1 is (0, 0)
each side of square is n long so the 4 corners are
(-n//2, -n//2), (n//2,-n//2), (-n//2, n//2) and (n//2, n//2)
"""

M = {(0, 1), (-1, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)}


def run(P, part):
    global M
    D = {(0, 0): 1}
    n = 1
    N = 1
    while True:
        loc = [n // 2 + 1, n // 2]
        for i in range(n):
            N += 1
            if part == 2:
                N = 0
                for d in M:
                    if (loc[0] + d[0], loc[1] + d[1]) in D:
                        N += D[(loc[0] + d[0], loc[1] + d[1])]
                D[tuple(loc)] = N
                if N >= P:
                    return N
            elif N >= P:
                return abs(loc[0]) + abs(loc[1])
            loc[1] -= 1
        for i in range(n + 1):
            N += 1
            if part == 2:
                N = 0
                for d in M:
                    if (loc[0] + d[0], loc[1] + d[1]) in D:
                        N += D[(loc[0] + d[0], loc[1] + d[1])]
                D[tuple(loc)] = N
                if N >= P:
                    return N
            elif N >= P:
                return abs(loc[0]) + abs(loc[1])
            loc[0] -= 1
        for i in range(n + 1):
            N += 1
            if part == 2:
                N = 0
                for d in M:
                    if (loc[0] + d[0], loc[1] + d[1]) in D:
                        N += D[(loc[0] + d[0], loc[1] + d[1])]
                D[tuple(loc)] = N
                if N >= P:
                    return N
            elif N >= P:
                return abs(loc[0]) + abs(loc[1])
            loc[1] += 1
        for i in range(n + 2):
            N += 1
            D[tuple(loc)] = N
            if part == 2:
                N = 0
                for d in M:
                    if (loc[0] + d[0], loc[1] + d[1]) in D:
                        N += D[(loc[0] + d[0], loc[1] + d[1])]
                D[tuple(loc)] = N
                if N >= P:
                    return N
            elif N >= P:
                return abs(loc[0]) + abs(loc[1])
            loc[0] += 1
        n += 2


print("part 1: ", run(347991, 1))
print("part 2: ", run(347991, 2))