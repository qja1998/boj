from collections import deque

N = int(input())

colors = [list(input()) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs(x, y):
    color = colors[x][y]
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if colors[nx][ny] != color:
                continue
            if visited[nx][ny]:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
    
    return 1


cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        cnt += bfs(i, j)


for i in range(N):
    for j in range(N):
        if colors[i][j] == 'G':
            colors[i][j] = 'R'

visited = [[False] * N for _ in range(N)]
cnt_weak = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        cnt_weak += bfs(i, j)

print(cnt, cnt_weak)