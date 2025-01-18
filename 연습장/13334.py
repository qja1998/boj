import heapq
import sys

input = sys.stdin.readline

N = int(input())

locations = [list(map(int, input().split()))[::-1] for _ in range(N)]
for i, (o, h) in enumerate(locations):
    # h < o 유지
    if h > o:
        locations[i] = [h, o]

heapq.heapify(locations)

rail_len = int(input())


start_q = []
ans = 0
cnt = 0
while locations:
    o, h = heapq.heappop(locations)

    # 통근 길이가 더 길면 제외
    if rail_len < o - h:
        continue

    heapq.heappush(start_q, h)

    # print(h, o, min_start)
    while start_q and o - start_q[0] > rail_len:
        heapq.heappop(start_q)

    # print(start_q)
    ans = max(ans, len(start_q))
    
print(ans)