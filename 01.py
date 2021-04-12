P = open("01.txt").readline().strip()

n = 0
for i in range(len(P)):
    if P[(i + 1) % len(P)] == P[i]:
        n += int(P[i])
print(f"Part 1: {n}")

n = 0
for i in range(len(P)):
    if P[(i + len(P) // 2) % len(P)] == P[i]:
        n += int(P[i])
print(f"Part 1: {n}")
