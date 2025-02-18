from collections import deque

M, N, H = map(int, input().split())

tomatos = []

for _ in range(H):
    tomatos.append([list(map(int, input().split())) for _ in range(N)])

dzs = [0, 0, 0, 0, 1, -1]
dys = [1, -1, 0, 0, 0, 0]
dxs = [0, 0, 1, -1, 0, 0]

visited = [[[False] * M for _ in range(N)] for _ in range(H)]
q = deque()

def search_tmt():
    while q:
        z, y, x = q.popleft()
        for dz, dy, dx in zip(dys, dxs, dzs):

            nz, ny, nx = z + dz, y + dy, x + dx

            if not(0 <= nz < H and 0 <= ny < N  and 0 <= nx < M):
                continue
            if visited[nz][ny][nx]:
                continue
            if tomatos[nz][ny][nx] != 0:
                continue
            
            tomatos[nz][ny][nx] = tomatos[z][y][x] + 1
            visited[nz][ny][nx] = True
            q.append((nz, ny, nx))

ans = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatos[z][y][x] < 1:
                continue
            q.append((z, y, x))
            visited[z][y][x] = True
search_tmt()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatos[z][y][x] == 0:
                print(-1)
                exit()
        ans = max(ans, max(tomatos[z][y]))
print(ans - 1)