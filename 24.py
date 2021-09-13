P = {
    tuple(map(lambda x: int(x), line.strip().split("/")))
    for line in open("24.txt", "r").readlines()
}


def bridge(lnk, length, strength, blocks, part):
    result = (length, strength)
    choices = {i for i in blocks if lnk in i}
    for ch in choices:
        lst = ch[1] if ch[0] == lnk else ch[0]
        t = bridge(lst, length + 1, strength + sum(ch), blocks - {ch}, part)
        if 1 == part and t[1] > result[1]:
            result = t
        if 2 == part and (t[0] > result[0] or (t[0] == result[0] and t[1] > result[1])):
            result = t
    return result


root = {i for i in P if i[0] == 0}.pop()
print(f"Part 1: {bridge(root[1], 1, root[1], P - {root}, 1)[1]}")
print(f"Part 2: {bridge(root[1], 1, root[1], P - {root}, 2)[1]}")
