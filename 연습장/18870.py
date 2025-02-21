import sys

import heapq
from collections import defaultdict

print = sys.stdout.write

N = int(input())
nums = list(map(int, input().split()))

order_dict = defaultdict(int)
q = list(set(nums))
heapq.heapify(q)

for i in range(len(q)):
    order_dict[heapq.heappop(q)] = i

for num in nums:
    print(f"{order_dict[num]} ")