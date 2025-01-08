# 행검사
def row_check(r, num):
    for x in range(9):
        if num == sdoku[r][x]:
            return False
    return True


def col_check(c, num):
    # 열검사
    for x in range(9):
        if num == sdoku[x][c]:
            return False
    return True


def three_check(r, c, num):
    # 3x3 검사
    nc = (c // 3) * 3
    nr = (r // 3) * 3
    for x in range(3):
        for y in range(3):
            if sdoku[nr + x][nc + y] == num:
                return False
    return True


def dfs(depth):
    if depth >= len(zero_p):
        for k in range(9):
            print(''.join(map(str, sdoku[k])))
        exit()

    nr, nc = zero_p[depth]  # 리스트에서 하나씩 튜플로 꺼낸다.
    for j in range(1, 9 + 1):
    	#dfs를 돌기전에 검사하여 조건에 맞는 것만 dfs를 돈다
        if row_check(nr, j) and col_check(nc, j) and three_check(nr, nc, j):
            sdoku[nr][nc] = j
            dfs(depth + 1)
            sdoku[nr][nc] = 0


sdoku = []
zero_p = []  # 2차원 9*9 리스트를 1차원적으로 생각하여 dfs를 돌기 때문에 좌표들을 튜플형식으로 넣는다.
for i in range(9):
    temp = list(map(int, input()))
    for j in range(len(temp)):
        if temp[j] == 0:
            zero_p.append((i, j))  # 0의 좌표들을 저장한다.(1차원 리스트에 튜플로 저장)
    sdoku.append(temp)

dfs(0)