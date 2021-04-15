from collections import deque

S = deque([0])
for i in range(1, 2018):
    S.rotate(-349)  # puzzle input
    S.append(i)
print(f"Part 1: {S.popleft()}")

S = deque([0])
for i in range(1, 50_000_001):
    S.rotate(-349)  # puzzle input
    S.append(i)
print(f"Part 2: {S[S.index(0)+1]}")
