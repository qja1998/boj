import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 5)

LOG = 21

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

graph = defaultdict(list)

for _ in range(N - 1):
    node1, node2, cost = map(int, input().split())
    graph[node1].append((node2, cost))
    graph[node2].append((node1, cost))

tree = defaultdict(list)
depth = [(0, 0) for _ in range(N + 1)]
parents = [[0] * LOG for _ in range(N + 1)]

def make_tree(node, cost, tree, graph, visited, d = 0):
    depth[node] = (d, cost)
    for n_node, n_cost in graph[node]:
        if visited[n_node]:
            continue
        tree[node].append((n_node, cost + n_cost))
        visited[n_node] = True
        parents[n_node][0] = node
        make_tree(n_node, cost + n_cost, tree, graph, visited, d + 1)

def set_parents(parents):
    for i in range(1, LOG):
        for node in range(1, N + 1):
            parents[node][i] = parents[parents[node][i - 1]][i - 1]

def get_ancestor(parents, node1, node2):
    if depth[node1][0] != depth[node2][0]:
        for i in range(LOG - 1, -1, -1):
            if depth[node2][0] - depth[node1][0] >= (1 << i):
                node2 = parents[node2][i]
    
    if node1 == node2:
        return node1
    
    for i in range(LOG - 1, -1, -1):
        if parents[node1][i] != parents[node2][i]:
            node1 = parents[node1][i]
            node2 = parents[node2][i]
    
    return parents[node1][0]


def get_dist(parents, node1, node2):
    # node2가 항상 더 깊도록
    if depth[node1][0] > depth[node2][0]:
        node1, node2 = node2, node1
    common_ancestor = get_ancestor(parents, node1, node2)
    # print(f"common_ancestor: {common_ancestor}\n")
    # print(depth[node1][1], depth[common_ancestor][1])
    # print(depth[node2][1], depth[common_ancestor][1])
    # print()
    
    dist = depth[node1][1] + depth[node2][1] - 2 * depth[common_ancestor][1]
    return dist

visited = [False] * (N + 1)
visited[1] = True
make_tree(1, 0, tree, graph, visited)
set_parents(parents)

M = int(input())
for _ in range(M):
    node1, node2 = map(int, input().split())
    print(f"{get_dist(parents, node1, node2)}\n")