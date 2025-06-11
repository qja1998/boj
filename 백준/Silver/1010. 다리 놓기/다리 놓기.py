from math import factorial

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    print(factorial(m) // (factorial(n) * factorial(m - n)))
