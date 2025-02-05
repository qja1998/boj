<<<<<<< HEAD
import heapq
=======
>>>>>>> 594e150527375a601f1d6cdedde81cb1b0c6826c
T = int(input())

for _ in range(T):
    K = int(input())

    res = 0
    files = list(map(int, input().split()))
    
    dp = [[0] * K for _ in range(K)]
    sum_list = [0] * (K + 1)

    # 누적합
    for i in range(K):
        sum_list[i + 1] = sum_list[i] + files[i]
    
    for i in range(1, K):
        for j in range(i, K):
            dp[j - i][j] = float('inf')
            for k in range(j - i, j):
                dp[j - i][j] = min(dp[j - i][j], dp[j - i][k] + dp[k + 1][j])
            dp[j - i][j] += sum_list[j + 1] - sum_list[j - i]
    
    print(dp[0][K - 1])
<<<<<<< HEAD
=======
    print(*dp, sep='\n')
>>>>>>> 594e150527375a601f1d6cdedde81cb1b0c6826c
