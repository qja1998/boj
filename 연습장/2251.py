from collections import deque

A, B, C = list(map(int, input().split()))

water_list = [0, 0, C]

def move_water(w1, w2, b2):
    remain = max(b2 - w2, 0)
    remain = min(remain, w1)

    w1 -= remain
    w2 += remain

    return w1, w2

result = set()
visited = []

q = deque([(0, 0, C)])
while q:
    a, b, c = q.popleft()
    if a == 0:
        result.add(c)

    # a -> b
    w1, w2 = move_water(a, b, B)
    if (w1, w2, c) not in visited:
        q.append((w1, w2, c))
        visited.append((w1, w2, c))
    
    # a -> c
    w1, w2 = move_water(a, c, C)
    if (w1, b, w2) not in visited:
        q.append((w1, b, w2))
        visited.append((w1, b, w2))
    
    # b -> a
    w1, w2 = move_water(b, a, A)
    if (w2, w1, c) not in visited:
        q.append((w2, w1, c))
        visited.append((w2, w1, c))
    
    # b -> c
    w1, w2 = move_water(b, c, C)
    if (a, w1, w2) not in visited:
        q.append((a, w1, w2))
        visited.append((a, w1, w2))

    # c -> a
    w1, w2 = move_water(c, a, A)
    if (w2, b, w1) not in visited:
        q.append((w2, b, w1))
        visited.append((w2, b, w1))

    # c -> b
    w1, w2 = move_water(c, b, B)
    if (a, w2, w1) not in visited:
        q.append((a, w2, w1))
        visited.append((a, w2, w1))

print(*sorted(list(result)))