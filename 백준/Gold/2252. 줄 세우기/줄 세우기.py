from collections import defaultdict, deque
N, M = map(int, input().split())
students = [[] for _ in range(N+1)]

start = set(i for i in range(1, N+1))
counter = [0] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    start -= set([b])
    students[a].append(b)
    counter[b] += 1

start = list(start)
depth_visit = defaultdict(list)

def bfs():
    q = deque(start)
    visited = [False] * (N+1)
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        # print(visited)
        # print(q)
        for i in students[cur]:
            if not visited[i]:
                counter[i] -= 1
                if counter[i] > 0:
                    continue
                visited[i] = True
                depth_visit[cur+1].append(i)
                q.append(i)

bfs()

# for i in range(1, N+1):
#     if depth_visit[i] == []:
#         break
#     print(*list(set(depth_visit[i])), sep=' ', end=' ')
