import sys
input = sys.stdin.readline
N = int(input())

matrics = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]

INF = float('inf')

for dif in range(1, N):
    # print('dif', dif)
    for i in range(0, N - dif):
        j = i + dif
        dp[i][j] = INF
        for k in range(dif):
            cost = (dp[i][i + k] + dp[i + k + 1][j])\
                  + (matrics[i][0] * matrics[i + k][1] * matrics[j][1])
            # print(i, j)
            # print(i + k)
            # print(dp[i][i + k][1][0], dp[i][i + k][1][1], dp[i + k + 1][j][1][1])
            # print(dp[i][i + k][0] + dp[i + k + 1][j][0], dp[i][i + k][1][0] * dp[i][i + k][1][1] * dp[i + k + 1][j][1][1])
            # print()
            dp[i][j]  = min(dp[i][j], cost)

# print(*dp, sep='\n')
print(dp[0][N - 1])