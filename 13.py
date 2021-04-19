# Each scanner with N layers, gets to the top at
# picoseconds i*(2*N-2). for example with 4 layers: 0, 6, 12, 18,...
# input packet reaches layer M at picosecond M.
# so if M % (2*N-2)==0, then there is a catch

L = [list(map(lambda x: int(x), line.strip().split(": "))) for line in open("13.txt").readlines()]
T = 0
for l in L:
    if l[0] % (2 * l[1] - 2) == 0:
        T += l[0] * l[1]
print(f"Part 1: {T}")

# brute force is probably easier than calculating Chinese remainders
for d in range(1_000_000_000):
    caught = False
    for l in L:
        if (d + l[0]) % (2 * l[1] - 2) == 0:
            caught = True
            break
    if caught:
        continue
    else:
        print(f"Part 2: {d}")
        break
