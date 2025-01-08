from collections import defaultdict, deque
import heapq

V, E = map(int, input().split())

K = int(input())

INF = float('inf')

graph = defaultdict(list)

dist = [INF] * (V + 1)
dist[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    
    while q:
        w, v = heapq.heappop(q)

        if dist[v] < w:
            continue
        
        for n_v, n_w in graph[v]:
            cost = dist[v] + n_w
            if cost < dist[n_v]:
                dist[n_v] = cost
                heapq.heappush(q, (cost, n_v))


dijkstra(K)

for d in dist[1:]:
    print(d if d != INF else 'INF')