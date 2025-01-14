import sys
import heapq

input = sys.stdin.readline

N, K  = map(int, input().split())

jewel_list = []

for _ in range(N):
    heapq.heappush(jewel_list, list(map(int, input().split())))

bags = sorted([int(input()) for _ in range(K)])

result = 0

tmp = []
for bag in bags:
    while jewel_list and bag >= jewel_list[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jewel_list)[1])
    if tmp:
        result -= heapq.heappop(tmp)
    elif not jewel_list:
        break

print(result)