P = list(map(lambda x: int(x), (line.strip() for line in open("05.txt").readlines())))


def part1(l):
    L = l.copy()
    pos = 0
    steps = 0
    while True:
        try:
            jmp = L[pos]
            L[pos] += 1
            pos += jmp
            steps += 1
        except IndexError:
            return steps


def part2(l):
    L = l.copy()
    pos = 0
    steps = 0
    while True:
        try:
            jmp = L[pos]
            if jmp >= 3:
                L[pos] -= 1
            else:
                L[pos] += 1
            pos += jmp
            steps += 1
        except IndexError:
            return steps


print(f"Part 1: {part1(P)}")
print(f"Part 2: {part2(P)}")
