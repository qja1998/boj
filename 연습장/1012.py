from collections import defaultdict, deque

T = int(input())

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def chk_area(xy, latt_map, visited):
    q = deque([xy])

    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nxy = (x + dx, y + dy)

            if not latt_map[nxy]:
                continue
            if nxy in visited:
                continue
            
            visited.append(nxy)
            q.append(nxy)
    
    return visited
        
    

for _ in range(T):
    M, N, K = map(int, input().split())

    latt_map = defaultdict(int)

    for _ in range(K):
        latt_map[(tuple(map(int, input().split())))] = 1
    
    visited = []
    cnt = 0
    xys = list(latt_map.keys())
    for xy in xys:
        if not latt_map[xy]:
            continue
        if xy in visited:
            continue
        visited = chk_area(xy, latt_map, visited + [xy])
        cnt += 1

    print(cnt)


