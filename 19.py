L = [line.replace("\n", "") for line in open("19.txt").readlines()]
loc = (0, L[0].find("|"))
d = (1, 0)
Letters = ""
D = {(1, 0), (0, 1), (0, -1), (-1, 0)}
Steps = 0

while True:
    Steps += 1
    loc = (loc[0] + d[0], loc[1] + d[1])
    if L[loc[0]][loc[1]] == "+":
        for newd in D - {(-d[0], -d[1])}:
            if L[loc[0] + newd[0]][loc[1] + newd[1]] != " ":
                d = newd
                break
    if L[loc[0]][loc[1]] not in "+|- ":
        Letters += L[loc[0]][loc[1]]
    elif L[loc[0]][loc[1]] == " ":
        break
print(f"Part 1: {Letters}")
print(f"Part 2: {Steps}")