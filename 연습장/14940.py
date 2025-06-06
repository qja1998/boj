from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)] # 그래프 생성
visited = [[-1] * M for _ in range(N)] # 방문기록
 
 # 방향탐색 범위설정
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]


def bfs(i,j):
    queue = deque()
    queue.append((i,j))

    visited[i][j] = 0

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if graph[nx][ny] == 0: # 갈 수 없는 땅 체크
                    visited[nx][ny] = 0
                elif graph[nx][ny] == 1: # 갈 수 있는 땅 체크
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()