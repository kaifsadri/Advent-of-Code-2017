Dance = open("16.txt").readline().strip().split(",")
P = "abcdefghijklmnop"
for step in Dance:
    if step[0] == "s":
        n = int(step[1:])
        P = P[16 - n :] + P[: 16 - n]
    elif step[0] == "x":
        c = step[1:].split("/")
        a, b = P[int(c[0])], P[int(c[1])]
        P = P.replace(b, "z").replace(a, b).replace("z", a)
    elif step[0] == "p":
        a, b = step[1:].split("/")
        P = P.replace(b, "z").replace(a, b).replace("z", a)
print(f"Part 1: {P}")

Dances = {"abcdefghijklmnop": "gkmndaholjbfcepi"}
P = "abcdefghijklmnop"
for _ in range(1000_000_000):
    try:
        P = Dances[P]
    except KeyError:
        temp = P
        for step in Dance:
            if step[0] == "s":
                n = int(step[1:])
                P = P[16 - n :] + P[: 16 - n]
            elif step[0] == "x":
                c = step[1:].split("/")
                a, b = P[int(c[0])], P[int(c[1])]
                P = P.replace(b, "z").replace(a, b).replace("z", a)
            elif step[0] == "p":
                a, b = step[1:].split("/")
                P = P.replace(b, "z").replace(a, b).replace("z", a)
        Dances[temp] = P
print(f"Part 2: {P}")