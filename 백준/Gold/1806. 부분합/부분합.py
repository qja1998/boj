N, S = map(int, input().split())

nums = list(map(int, input().split()))

# S 이상, 가장 수열의 길이가 작은

total = sum(nums)

l, r = 0, 0

sum_num = 0

min_len = float('inf')

while True:
    if sum_num >= S:
        # S보다 클 때
        min_len = min(min_len, r - l)
        sum_num -= nums[l]
        l += 1
    elif r == N:
        break
    else:
        # S보다 작을 때
        sum_num += nums[r]
        r += 1

if min_len == float('inf'):
    print(0)
else:
    print(min_len)