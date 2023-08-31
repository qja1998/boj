import sys
from collections import defaultdict
input = sys.stdin.readline

num = input()
cnt_dict = defaultdict(int)
for i in num:
    cnt_dict[i] += 1
ans = ''
for i in sorted(cnt_dict, reverse=True):
    for _ in range(cnt_dict[i]):
        ans += i

print(ans)