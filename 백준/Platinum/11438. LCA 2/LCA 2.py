import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n = int(input())

LOG = 21

d_list = [0] * (n + 1)
chk_list = [False] * (n + 1)
parents = [[0] * LOG for _ in range(n + 1)]

tree = [[] for _ in range(n + 1)]
for _ in range(n-1):
    p, c = map(int, input().split())
    tree[p].append(c)
    tree[c].append(p)

def dfs(tree, node=1, depth=0):
    d_list[node] = depth
    chk_list[node] = True
    
    for c in tree[node]:
        if chk_list[c]:
            continue
        parents[c][0] = node
        dfs(tree, c, depth + 1)
        
def set_parent(tree):
    dfs(tree)
    for i in range(1, LOG):
        for node in range(1, len(parents)):
            parents[node][i] = parents[parents[node][i-1]][i-1]

def lca(a, b):
    if d_list[a] > d_list[b]:
        a, b = b, a

    for i in range(LOG - 1, -1, -1):
        # 깊이 차이가 2제곱수보다 더 크면 깊은 쪽을 그만큼 올림
        if d_list[b] - d_list[a] >= 2 ** i:
            b = parents[b][i]

    if a == b:
        return a
    
    for i in range(LOG - 1, -1, -1):
        if  parents[a][i] != parents[b][i]:
            a = parents[a][i]
            b = parents[b][i]

    return parents[a][0]

set_parent(tree)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))