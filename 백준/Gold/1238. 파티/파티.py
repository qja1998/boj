from collections import defaultdict
import heapq

N, M, X = map(int, input().split())

INF = float('inf')

# g = [[INF] for _ in range(N + 1)]
# g_rev = [[INF] for _ in range(N + 1)]

g = defaultdict(list)
g_rev = defaultdict(list)

for _ in range(M):
    s, e, t = map(int, input().split())
    g[s].append((t, e))
    g_rev[e].append((t, s))

def dijkstra(g, end):
    dist = [INF] * (N + 1)
    dist[0] = 0
    dist[end] = 0
    q = [(0, end)]

    while q:
        t, node = heapq.heappop(q)
        for t, n_node in g[node]:
            if dist[n_node] > dist[node] + t:
                dist[n_node] = dist[node] + t
                heapq.heappush(q, (dist[n_node], n_node))
    return dist

result = zip(dijkstra(g, X), dijkstra(g_rev, X))
ans = 0
for d, d_rev in result:
    if d + d_rev == INF:
        continue
    ans = max(ans, d + d_rev)

print(ans)