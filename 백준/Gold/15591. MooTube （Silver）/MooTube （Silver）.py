from collections import deque

# 영상에 대해 유사도가 K 이상인 모든 동영상 추천

N, Q = map(int, input().split())
INF = float('inf')

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

visited = [[False] * (N + 1) for _ in range(N + 1)]

# print(*graph, sep='\n')

def get_relations(graph, start, k):
    q = deque([(start, INF)])
    visited = [False] * (N + 1)
    visited[start] = True
    cnt = 0

    while q:
        node, min_r = q.popleft()

        for n_node, r in graph[node]:
            if visited[n_node]:
                continue
            visited[n_node] = True
            r = min(min_r, r)
            if r >= k:
                cnt += 1
            q.append((n_node, r))
    return cnt
        
        
for _ in range(Q):
    k, v = map(int, input().split())

    print(get_relations(graph, v, k))