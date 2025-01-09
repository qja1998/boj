T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    dp = [[0] * K for _ in range(K)]
    sum_arr = [0] * (K + 1)
    for i in range(1, K + 1):
        sum_arr[i] = sum_arr[i - 1] + files[i - 1]

    for gap in range(1, K):
        for i in range(K - gap):
            j = i + gap
            dp[i][j] = float('inf')

            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + sum_arr[j + 1] - sum_arr[i])

    print(dp[0][K - 1])