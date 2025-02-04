from math import factorial
def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

N = int(input())

ans = 0

for i in range(1, N // 4 + 1):
    ans += comb(13, i) * comb(52 - 4*i, N - 4*i) * ((-1) ** (i + 1)) % 10_007

print(ans % 10_007)