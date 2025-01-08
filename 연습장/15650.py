from itertools import permutations
from collections import defaultdict

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

visited = defaultdict(bool)
for comb in permutations(nums, M):
    if visited[comb]:
        continue
    print(*list(comb))
    visited[comb] = True