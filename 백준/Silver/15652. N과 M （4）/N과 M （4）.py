import sys
from itertools import combinations_with_replacement

print = sys.stdout.write

N, M = map(int, input().split())

nums = [str(i + 1) for i in range(N)]

for comb in combinations_with_replacement(nums, M):
    print(f"{' '.join(comb)}\n")