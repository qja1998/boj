s1 = '-' + input()
s2 = '-' + input()

n1 = len(s1)
n2 = len(s2)

dp = [['' for _ in range(n1)] for _ in range(n2)]

for i in range(1, n2):
    for j in range(1, n1):
        if s1[j] == s2[i]:
            dp[i][j] = dp[i-1][j-1] + s1[j]
            continue

        if len(dp[i][j-1]) > len(dp[i-1][j]):
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = dp[i-1][j]


print(len(dp[-1][-1]))
if len(dp[-1][-1]):
    print(dp[-1][-1])
