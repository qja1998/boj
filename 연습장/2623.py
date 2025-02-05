from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
counter = [0 for _ in range(N+1)]
start = set(i for i in range(1, N+1))

for _ in range(M):
    _, *singers = list(map(int, input().split()))

    for singer1, singer2 in zip(singers[:-1], singers[1:]):
        graph[singer1].append(singer2)
        counter[singer2] += 1
        start -= set([singer2])

q = deque(start)

result = []

while q:
    singer = q.popleft()
    result.append(singer)
    for n_singer in graph[singer]:
        counter[n_singer] -= 1
        if counter[n_singer] > 0:
            continue
        q.append(n_singer)

if len(result) == N:
    print(*result, sep='\n')
else:
    print(0)