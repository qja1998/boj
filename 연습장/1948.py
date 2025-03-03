import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
graph_rev = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())

    graph[s].append((-c, e))
    graph_rev[e].append((-c, s))

start, end = map(int, input().split())

def search_path(graph, start):
    q = [(0, start)]
    visited = [False] * (n + 1)
    visited[start] = True
    
    dist = [0] * (n + 1)

    while q:
        _, node = heapq.heappop(q)
        visited[node] = True
        for n_cost, n_node in graph[node]:
            if visited[n_node]:
                continue
            n_cost *= -1
            if dist[n_node] < dist[node] + n_cost:
                dist[n_node] = dist[node] + n_cost
                heapq.heappush(q, (-n_cost, n_node))
    
    return dist

dist = search_path(graph, start)
dist_rev = search_path(graph_rev, start)

print(dist)
print(dist_rev)