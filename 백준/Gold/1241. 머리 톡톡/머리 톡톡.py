import sys
from collections import Counter, defaultdict

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

students = [int(input()) for _ in range(N)]
MAX_STUDENT = max(students) + 1

counter = Counter(students)
toktok = defaultdict(int)

for i in range(1, MAX_STUDENT):
    for j in range(i, MAX_STUDENT, i):
        if j in counter:
            # print(f"{i} {j} {counter[j]}\n")
            toktok[j] += counter[i]
# print(str(toktok))
# print(str(students))
print("\n".join(str(toktok[s] - 1) for s in students) + "\n")