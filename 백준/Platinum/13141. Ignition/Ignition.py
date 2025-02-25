INF = float('inf')

N, M = map(int, input().split())

def calculrate_dist(g, n):
    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                if i == j:
                    continue
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    return g

g = [[INF] * (N + 1) for _ in range(N + 1)]
g_max = [[-1] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    s, e, l = map(int, input().split())

    g[s][e] = min(g[s][e], l)
    g[e][s] = min(g[e][s], l)

    g_max[s][e] = max(g_max[s][e], l)
    g_max[e][s] = max(g_max[e][s], l)

for i in range(N + 1):
    g[i][i] = 0
    g[i][0] = 0
    g[0][i] = 0

g = calculrate_dist(g, N + 1)

ans = INF
for node in range(1, N + 1):
    part_ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if g_max[i][j] == -1:
                continue
            
            remain_rope = g_max[i][j] - abs(g[node][i] - g[node][j])
            part_ans = max(part_ans, max(g[node][i],  g[node][j]) + remain_rope / 2)
    
    ans = min(ans, part_ans)

print(ans)