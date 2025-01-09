from bisect import bisect_left

N = int(input())

nums = list(map(int, input().split()))

max_idx = 0

lis = [nums[0]]
lis_ids = [(nums[0], 0)]

for num in nums[1:]:
    idx = bisect_left(lis, num)
    if len(lis) == idx:
        lis.append(num)
        max_idx = idx
    else:
        lis[idx] = num
    lis_ids.append((num, idx))

# print(lis_ids)
print(len(lis))
result = []
pre = max_idx + 1
for num, i in lis_ids[::-1]:
    # print(num, i)
    # print(pre)
    if pre - 1 == i:
        result.append(num)
        pre = i
print(*result[::-1])