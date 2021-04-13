from collections import defaultdict

L = [line.strip().split() for line in open("08.txt").readlines()]
R = defaultdict(int)


def condition(reg, cond, value):
    global R
    r = R[reg]
    v = int(value)
    if cond == "!=":
        return r != v
    elif cond == ">=":
        return r >= v
    elif cond == ">":
        return r > v
    elif cond == "<":
        return r < v
    elif cond == "<=":
        return r <= v
    elif cond == "==":
        return r == v


M = 0
for line in L:
    r = line[0]
    val = int(line[2])
    if line[1] == "inc":
        if condition(line[4], line[5], line[6]):
            R[r] += val
    elif line[1] == "dec":
        if condition(line[4], line[5], line[6]):
            R[r] -= val
    if (m := max(R.values())) > M:
        M = m


print(f"Part 1: {max(R.values())}")
print(f"Part 2: {M}")