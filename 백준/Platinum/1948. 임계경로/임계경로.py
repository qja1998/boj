import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())


graph = [[] for _ in range(n + 1)]
graph_rev = [[] for _ in range(n + 1)]

in_cnt = [0] * (n + 1)

for _ in range(m):
    s, e, c = map(int, input().split())

    graph[s].append((e, c))
    in_cnt[e] += 1

    graph_rev[e].append((s, c))

start, end = map(int, input().split())

q = deque([(start, 0)])
path_counter = [0] * (n + 1)
max_cost = [0] * (n + 1)

# 각 노드에 도착하는 최대 시간간 저장
while q:
    node, cost = q.popleft()

    for n_node, n_cost in graph[node]:
        in_cnt[n_node] -= 1
        if max_cost[n_node] < cost + n_cost:
            max_cost[n_node] = cost + n_cost
        # 다 도착하면 출발하고, 제일 마지막에 온 경우만 추가 = cost가 가장 큰 경우
        if in_cnt[n_node] == 0:
            q.append((n_node, max_cost[n_node]))
# print(max_cost)

# 거꾸로가면서 도로 수 확인
path_cnt = 0
q = deque([(end, max_cost[end])])
visited = [False] * (n + 1)
visited[end] = True

while q:
    node, cost = q.popleft()

    for n_node, n_cost in graph_rev[node]:

        n_cost = cost - n_cost
        if n_cost != max_cost[n_node]:
            continue
        path_cnt += 1
        if visited[n_node]:
            continue
        # print(n_node)
        # print(cost, n_cost)
        visited[n_node] = True
        q.append((n_node, n_cost))
        


print(max_cost[end])
print(path_cnt)