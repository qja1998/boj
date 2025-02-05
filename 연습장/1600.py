from collections import deque

K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

dyx = ((1, 0), (-1, 0), (0, 1), (0, -1))
dyx_h = ((1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1))

q = deque([(0, 0, 0)])

visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
visited[0][0][0] = 1

available = False
while q:
    y, x, h_cnt = q.popleft()

    if (x, y) == (W - 1, H - 1):
        ans = visited[y][x][h_cnt] - 1
        available = True
        break
    
    # 나이트 이동
    for dy, dx in dyx:
        ny, nx = y + dy, x + dx

        # 범위 벗어남
        if not (0 <= ny < H and 0 <= nx < W):
            continue
        # 장애물
        if grid[ny][nx]:
            continue
        # 이미 방문함
        if visited[ny][nx][h_cnt]:
            continue

        visited[ny][nx][h_cnt] = visited[y][x][h_cnt] + 1
        q.append((ny, nx, h_cnt))


    if h_cnt < K:
        for dy, dx in dyx_h:
            ny, nx = y + dy, x + dx

            # 범위 벗어남
            if not (0 <= ny < H and 0 <= nx < W):
                continue
            # 장애물
            if grid[ny][nx]:
                continue
            # 이미 방문함
            if visited[ny][nx][h_cnt + 1]:
                continue
        
            visited[ny][nx][h_cnt + 1] = visited[y][x][h_cnt] + 1
            q.append((ny, nx, h_cnt + 1))

print(ans if available else -1)