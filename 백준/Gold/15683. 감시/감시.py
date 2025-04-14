import sys




N, M = map(int, input().split())
office_map = [list(map(int, input().split())) for _ in range(N)]

cctv = []
initial_zeros = 0 

for y in range(N):
    for x in range(M): 
        if 1 <= office_map[y][x] <= 5:
            cctv.append((office_map[y][x], y, x)) 
        elif office_map[y][x] == 0:
            initial_zeros += 1

cctv_num = len(cctv)


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


cctv_directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

max_covered_zeros = 0 


def get_covered_in_direction(y, x, direction_idx):
    covered_set = set()
    cdy, cdx = dy[direction_idx], dx[direction_idx]
    ny, nx = y + cdy, x + cdx 

    while 0 <= ny < N and 0 <= nx < M:
        if office_map[ny][nx] == 6: 
            break
        if office_map[ny][nx] == 0: 
            covered_set.add((ny, nx))
        
        ny, nx = ny + cdy, nx + cdx
    return covered_set


def solve(cctv_idx, current_covered_set):
    global max_covered_zeros

    
    if cctv_idx == cctv_num:
        max_covered_zeros = max(max_covered_zeros, len(current_covered_set))
        return

    cctv_type, y, x = cctv[cctv_idx]

    for directions in cctv_directions[cctv_type]:
        newly_covered_by_this_cctv = set()
        
        for d_idx in directions:
            newly_covered_by_this_cctv.update(get_covered_in_direction(y, x, d_idx))

        
        solve(cctv_idx + 1, current_covered_set.union(newly_covered_by_this_cctv))


solve(0, set())


print(initial_zeros - max_covered_zeros)