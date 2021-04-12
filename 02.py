L = [set(map(lambda x: int(x), line.strip().split())) for line in open("02.txt").readlines()]

print(f"Part 1: {sum({max(line) - min(line) for line in L})}")

n = 0
for line in L:
    for t in line:
        b = False
        for u in line - {t}:
            if t % u == 0:
                b = True
                n += t // u
                break
        if b:
            break
print(f"Part 2: {n}")
