from collections import defaultdict

L = [line.strip().split() for line in open("08.txt").readlines()]
R = defaultdict(int)


M = 0
for l in L:
    e = (
        "R['"
        + l[0]
        + "']"
        + l[1].replace("inc", "+=").replace("dec", "-=")
        + l[2]
        + " if "
        + "R['"
        + l[4]
        + "']"
        + l[5]
        + l[6]
        + " else 0"
    )
    exec(e)
    if (m := max(R.values())) > M:
        M = m


print(f"Part 1: {max(R.values())}")
print(f"Part 2: {M}")