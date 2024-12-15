import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

result = [nums[0]]

for item in nums:
    if result[-1] < item:
        result.append(item)
    else:
        idx = bisect_left(result, item)
        result[idx] = item

print(len(result))
