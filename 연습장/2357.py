import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

N, M  = map(int, input().split())

nums = [int(input()) for _ in range(N)]

# dp를 우선순위 큐로 완성
dp = [[]]

for _ in range(M):
    a, b = map(int, input().split())