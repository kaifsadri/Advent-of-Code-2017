P = open("09.txt").readline().strip()

p1 = 0
p2 = 0
cur = 0
gar = False
pos = 0
while pos < len(P):
    c = P[pos]
    if gar:
        if c == "!":
            pos += 1  # Skip
        elif c == ">":
            gar = False
        else:
            p2 += 1  # count valid garbage chars
    else:
        if c == "<":
            gar = True
        elif c == "{":
            cur += 1
            p1 += cur
        elif c == "}":
            cur -= 1
    pos += 1
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")