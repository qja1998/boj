from collections import deque, defaultdict

dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def show(dust, purifier):
    tmp = [[0]*C for _ in range(R)]
    for x, y in dust:
        # print(x, y)
        tmp[y][x] = dust[(x, y)]
    for x, y in purifier:
        tmp[y][x] = -1
    return tmp

def dust_diffuse(dust_map, R, C):
    """
    1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
    (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
    인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
    확산되는 양은 A_{r,c}/5이고 소수점은 버린다. 즉, ⌊A_{r,c}/5⌋이다.
    (r, c)에 남은 미세먼지의 양은 A_{r,c} - ⌊A_{r,c}/5⌋×(확산된 방향의 개수) 이다.
    """

    diffuse = defaultdict(int)
    for y in range(R):
        for x in range(C):
            if dust_map[y][x] <= 0:
                continue
            diffuse_dust = dust_map[y][x] // 5

            for dx, dy in dxy:
                nx, ny = x + dx, y + dy

                # 범위 벗어남
                if not (0 <= nx < C and 0 <= ny < R):
                    continue

                # 비어있지 않음
                if dust_map[ny][nx] == -1:
                    continue

                dust_map[y][x] -= diffuse_dust
                diffuse[(nx, ny)] += diffuse_dust

    for x, y in diffuse:
        dust_map[y][x] += diffuse[(x, y)]


def do_purifier(dust_map, purifier_up, purifier_down, R, C):
    """
    2. 공기청정기가 작동한다.
    공기청정기에서는 바람이 나온다.
    위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
    공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
    """

    # 위쪽 회전
    up_line = []
    up_x, up_y = purifier_up
    
    # 공기청정기 기준 반시계로 (모서리는 가로에 포함)
    len_list = []
    up_line += dust_map[up_y][up_x + 1:]
    len_list.append(len(up_line))

    up_line += [dust_map[i][C-1] for i in range(up_y-1, 0, -1)]
    len_list.append(len(up_line))

    up_line += dust_map[0][::-1]
    len_list.append(len(up_line))

    up_line += [dust_map[i][0] for i in range(1, up_y)]
    len_list.append(len(up_line))

    up_line += dust_map[up_y][0:up_x]
    len_list.append(len(up_line))

    # 반시계 회전
    up_line = [0] + up_line[:-1]



    # map에 적용
    line_list = [up_line[:len_list[0]],
                 up_line[len_list[0]:len_list[1]],
                 up_line[len_list[1]:len_list[2]],
                 up_line[len_list[2]:len_list[3]],
                 up_line[len_list[3]:]]
    
    # print(line_list)

    dust_map[up_y][up_x + 1:] = line_list[0]

    for i in range(len_list[1] - len_list[0]):
        dust_map[i+1][C-1] = line_list[1][len_list[1] - len_list[0] - i - 1]

    dust_map[0][::-1] = line_list[2]

    for i in range(len_list[3] - len_list[2]):
        dust_map[i+1][0] = line_list[3][i]

    dust_map[up_y][:up_x] = line_list[4]


    # 아래쪽 회전
    down_line = []
    down_x, down_y = purifier_down
    
    # 공기청정기 기준 시계로 (모서리는 가로에 포함)
    len_list = []
    down_line += dust_map[down_y][down_x + 1:]
    len_list.append(len(down_line))

    down_line += [dust_map[i][C-1] for i in range(down_y+1, R-1)]
    len_list.append(len(down_line))

    down_line += dust_map[R-1][::-1]
    len_list.append(len(down_line))

    down_line += [dust_map[i][0] for i in range(R-2, down_y, -1)]
    len_list.append(len(down_line))

    down_line += dust_map[down_y][0:down_x]
    len_list.append(len(down_line))

    # 시계 회전
    down_line = [0] + down_line[:-1]

    # map에 적용
    line_list = [down_line[:len_list[0]],
                 down_line[len_list[0]:len_list[1]],
                 down_line[len_list[1]:len_list[2]],
                 down_line[len_list[2]:len_list[3]],
                 down_line[len_list[3]:]]
    

    # print(line_list)

    dust_map[down_y][down_x + 1:] = line_list[0]

    for i in range(len_list[1] - len_list[0]):
        dust_map[down_y+i+1][C-1] = line_list[1][i]

    dust_map[R-1][::-1] = line_list[2]

    for i in range(len_list[3] - len_list[2]):
        dust_map[down_y+i+1][0] = line_list[3][len_list[3] - len_list[2] - i - 1]

    dust_map[down_y][:down_x] = line_list[4]


R, C, T = map(int, input().split())

purifier = []

dust_map = []

for y in range(R):
    row = []
    for x, val in enumerate(map(int, input().split())):
        row.append(val)
        if val == -1:
            purifier.append((x, y))
    dust_map.append(row)

purifier_up = purifier[0]
purifier_down = purifier[1]

for _ in range(T):
    dust_diffuse(dust_map, R, C)
    do_purifier(dust_map, purifier_up, purifier_down, R, C)

result = 0

for y in range(R):
    for x in range(C):
        if dust_map[y][x] <= 0:
            continue
        result += dust_map[y][x]

print(result)