from collections import defaultdict, deque

N = int(input())

g = defaultdict(list)


for _ in range(N-1):
    p, c, w = map(int, input().split())
    g[p].append((c, w))
    g[c].append((p, w))

ROOT = 1

# 가장 깊은 부분 찾기

max_distance = 0
max_node = 1

q = deque([(1, 0)])
visited = [1]

while q:
    # print(q)
    p, w = q.popleft()


    if max_distance < w:
        max_distance = w
        max_node = p

    for c, c_w in g[p]:
        if c in visited:
            continue
        q.append(((c, c_w + w)))
        visited.append(c)

# print(max_node, max_distance)
# 가장 깊은 곳부터 가장 먼 곳까지 탐색

q = deque([(max_node, 0)])
visited = [max_node]

max_distance = 0
max_node = 1

while q:
    p, w = q.popleft()

    if max_distance < w:
        max_distance = w
        max_node = p

    for c, c_w in g[p]:
        if c in visited:
            continue
        q.append((c, c_w + w))
        visited.append(c)

print(max_distance)