from collections import Counter

D = Counter()
state = "A"  # puzzle input
pos = 0
for i in range(12172063):  # puzzle input
    if state == "A":
        if D[pos] == 0:
            D[pos] = 1
            pos += 1
            state = "B"
        elif D[pos] == 1:
            D[pos] = 0
            pos -= 1
            state = "C"
    elif state == "B":
        if D[pos] == 0:
            D[pos] = 1
            pos -= 1
            state = "A"
        elif D[pos] == 1:
            # D[pos] = 1
            pos -= 1
            state = "D"
    elif state == "C":
        if D[pos] == 0:
            D[pos] = 1
            pos += 1
            state = "D"
        elif D[pos] == 1:
            D[pos] = 0
            pos += 1
            state = "C"
    elif state == "D":
        if D[pos] == 0:
            # D[pos] = 0
            pos -= 1
            state = "B"
        elif D[pos] == 1:
            D[pos] = 0
            pos += 1
            state = "E"
    elif state == "E":
        if D[pos] == 0:
            D[pos] = 1
            pos += 1
            state = "C"
        elif D[pos] == 1:
            # D[pos] = 1
            pos -= 1
            state = "F"
    elif state == "F":
        if D[pos] == 0:
            D[pos] = 1
            pos -= 1
            state = "E"
        elif D[pos] == 1:
            # D[pos] = 1
            pos += 1
            state = "A"

print(f"Part 1: {sum(D.values())}")
