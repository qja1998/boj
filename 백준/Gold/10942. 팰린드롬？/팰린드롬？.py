import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
nums = list(map(int, input().split()))

M = int(input())

dp = [[False]*N for _ in range(N)]

for i in range(N):
    dp[i][i] = True

for i in range(N-1):
    dp[i][i+1] = nums[i] == nums[i+1]

# from pprint import pprint
# pprint(dp)

# for i in range(N-1):
#     for j in range(i+1, N):
#         dp[(i, j)] = dp[(i+1, j-1)] and nums[i] == nums[j]

for i in range(2, N):
    for j in range(N-i):
        dp[j][j+i] = dp[j+1][j+i-1] and nums[j] == nums[j+i]

# pprint(dp)
for _ in range(M):
    S, E = map(int, input().split())
    print("1\n" if dp[S-1][E-1] else "0\n")