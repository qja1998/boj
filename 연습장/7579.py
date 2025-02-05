N, M = map(int, input().split())

memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [[0] * (M+1) for _ in range(N)]

# 첫 번째 memory 값 초기화
for i in range(memories[0] + 1):
    dp[0][i] = costs[0]

sum_mem = memories[0]
for i in range(1, N):
    cur_mem = memories[i]
    for j in range(cur_mem + 1):
        dp[i][j] = dp[i - 1][j]
    for j in range(cur_mem + 1, min(M+1, cur_mem + sum_mem + 1)):
        dp[i][j] = min(costs[i] + dp[i - 1][j - (cur_mem + 1)], dp[i - 1][j])
    
    sum_mem += cur_mem

print(dp[-1][-1])

print(*dp, sep='\n')



##########################################################
"""import sys

N, M = map(int, sys.stdin.readline().split())
memories = [0] + list(map(int, sys.stdin.readline().split()))
cost = [0] + list(map(int, sys.stdin.readline().split()))

dp = [ [0] * (sum(cost) + 1) for _ in range(N + 1) ]

answer = sum(cost)

for i in range(1, N + 1):
    for j in range(sum(cost) + 1):
        dp[i][j] = dp[i - 1][j]

    for j in range(cost[i], sum(cost) + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + memories[i])
        if (dp[i][j] >= M):
            answer = min(answer, j)

print(answer)"""