import sys
sys.setrecursionlimit(10 ** 9)

from collections import defaultdict

input = sys.stdin.readline
tree = defaultdict(list)

N = int(input())

for _ in range(N-1):
    u, v = map(int, input().split())

    tree[u].append(v)
    tree[v].append(u)

result = float('inf')
dp = [[0, 1] for _ in range(N+1)]
visited=[False]*(N+1)

def dfs(node):
    visited[node]=True
    for n_node in tree[node]:
        if(visited[n_node]):
            continue
        dfs(n_node)
        dp[node][0]+=dp[n_node][1]
        dp[node][1]+=min(dp[n_node])

start = 1 

dfs(start)

print(min(dp[start]))