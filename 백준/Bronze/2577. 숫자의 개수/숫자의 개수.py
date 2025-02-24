from collections import defaultdict
d = defaultdict(int)
num = 1
for _ in range(3):
    num *= int(input())
for c in str(num):
    d[c] += 1
for i in range(10):
    print(d[str(i)])