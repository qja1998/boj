import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

cost = [0] * (N+1)
weight = [0] * (N+1)
impossible = False
INF = float("INF")
new_x = set()
def dfs(node, node_cost, a):
    global impossible, new_x

    if cost[node]:
        curr_a, curr_cost = cost[node]

        if curr_a == a:
            if curr_cost != node_cost:
                impossible = True
        else:
            if (node_cost - curr_cost) % 2 == 1:
                impossible = True
            else:
                tmp_x = curr_a * (node_cost - curr_cost) // 2
                new_x.add(tmp_x)

        return

    cost[node] = (a, node_cost)
    weight[node] = -a * node_cost

    for nxt, edge_cost in arr[node]:
        dfs(nxt, edge_cost - node_cost, -a)

    return

dfs(1, 0, 1)

if 1 < len(new_x) or impossible:
    print("No")
else:
    if new_x:
        x = new_x.pop()
    else:
        weight.sort()
        x = weight[(N+1) // 2]

    print("Yes")
    for a, c in cost[1:]:
        print(a * x + c, end=" ")
    print()
