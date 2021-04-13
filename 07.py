L = [line.strip() for line in open("07.txt").readlines()]
C = dict()  # children
W = dict()  # weights
for line in L:
    t = line.split()
    W[t[0]] = int(t[1][1:-1])
    if "->" in t:
        C[t[0]] = [i.replace(",", "") for i in t[3:]]  # C[parent] = [child, child, child]


def find_root():
    global C
    for p in C:
        found = True
        for k in C.values():
            if p in k:
                found = False
                continue
        if found:
            break
    return p


def weigh(k):
    global W, C
    w = W[k]
    try:
        for i in C[k]:
            w += weigh(i)
    except KeyError:
        pass
    return w


R = find_root()
print(f"Part 1: {R}")

ToGo = [R]
result = 0
while ToGo:
    node = ToGo.pop()
    try:
        children = C[node]
        w = weigh(children[0])
        for c in children[1:]:
            if weigh(c) != w:
                nodewts = [W[i] for i in children]
                towerwts = [weigh(i) for i in children]
                for i, item in enumerate(towerwts):
                    if towerwts.count(item) == 1:
                        result = nodewts[i] + (towerwts[(i + 1) % len(towerwts)] - towerwts[i])
        ToGo += children
    except KeyError:
        pass
print(f"Part 2: {result}")
