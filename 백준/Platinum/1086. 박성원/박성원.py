import sys

input = sys.stdin.readline

def gcd(a: int, b: int):
    if b == 0:
        return a
    return gcd(b, a % b)

N = int(input())
arr = [int(input()) for _ in range(N)]
K = int(input())
dp = [[0] * K for _ in range(1 << N)]
dp[0][0] = 1

next_vals = []
for l in range(N):
    temp = []
    for j in range(K):
        temp.append((j * (10 ** (len(str(arr[l]))) % K) + (arr[l] % K)) % K)
    next_vals.append(temp)

for i in range(1 << N):
    for l in range(N):
        if i & (1 << l):
            continue
        for j in range(K):
            next_val = next_vals[l][j]
            dp[i | (1 << l)][next_val] += dp[i][j]
p = dp[(1 << N) - 1][0]
q = sum(dp[(1 << N) - 1])
g = gcd(p, q)
print(f"{p // g}/{q // g}")