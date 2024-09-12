from collections import deque

N = int(input())
K = int(input())
apple_location = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
change_info = [list(map(str, input().split())) for _ in range(L)]


def show_map(snake):
    matrix = [[0] * N for _ in range(N)]
    for y, x in snake:
        matrix[y][x] = 1

    return matrix

# 우 하 좌 상
move = ((0, 1), (1, 0), (0, -1), (-1, 0))

snake = deque([(0, 0)])
count = 0
way = 0
pan = 0
time_cum = 0
for time, path in change_info:
    dy = move[way][0]
    dx = move[way][1]
    for _ in range(int(time) - time_cum):
        ny, nx = dy + snake[-1][0], dx + snake[-1][1]
        if not (0 <= ny < N) or not (0 <= nx < N):
            count += 1
            print(count)
            exit()
        else:
            if [ny + 1, nx + 1] in apple_location:
                apple_location.remove([ny + 1, nx + 1])
                snake.append((ny, nx))
                count += 1
            else:
                count += 1
                if (ny, nx) in snake:
                    print(count)
                    exit()
                snake.append((ny, nx))
                snake.popleft()

    if path == 'L':
        way = abs(way + 3) % 4
    else:
        way = abs(way + 1) % 4
    time_cum = int(time)

dy = move[way][0]
dx = move[way][1]
while True:
    ny, nx = dy + snake[-1][0], dx + snake[-1][1]
    if not (0 <= ny < N) or not (0 <= nx < N):
        count += 1
        print(count)
        exit()
    else:
        if [ny + 1, nx + 1] in apple_location:
            apple_location.remove([ny + 1, nx + 1])
            snake.append((ny, nx))
            count += 1
        else:
            count += 1
            if (ny, nx) in snake:
                print(count)
                exit()
            snake.append((ny, nx))
            snake.popleft()