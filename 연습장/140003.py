from bisect import bisect_left

N = int(input())

nums = list(map(int, input().split()))

max_len = 0
ans = []
result = [float('-inf')]
for i, num in enumerate(nums[:-1]):
    idx = bisect_left(result, num)

    if idx == len(result):
        result.append(num)
    else:
        result = result[:idx+1]
        result[idx] = num
    
    if len(result) > max_len:
        max_len = len(result[1:])
        ans = result[1:]


print(max_len)
print(*result[1:], sep=' ')
