from collections import deque

N, M = map(int, input().split())

dxy = ((1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1))

x, y = map(int, input().split())

enemy_list = [tuple(map(int, input().split())) for _ in range(M)]
result = [0] * M

q = deque([(x, y, 1)])
find_cnt = 0
visited = set([(x, y)])

while q:
    cur_x, cur_y, t = q.popleft()

    for dx, dy in dxy:
        n_x, n_y = cur_x + dx, cur_y + dy
        if (n_x, n_y) in visited:
            continue
        if (n_x, n_y) in enemy_list:
            enemy_idx = enemy_list.index((n_x, n_y))
            if result[enemy_idx] != 0:
                continue
            result[enemy_idx] = t
            find_cnt += 1
        # print(result)
        # print(find_cnt, M)
        if find_cnt == M:
            break
        q.append((n_x, n_y, t + 1))
        visited.add((n_x, n_y))
    else:
        continue
    break

print(*result)