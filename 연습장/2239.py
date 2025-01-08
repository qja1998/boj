num_map = [list(map(int, list(input()))) for _ in range(9)]

# 빈칸 위치 저장
blank_pos = []

for y in range(9):
    for x in range(9):
        if num_map[y][x] == 0:
            blank_pos.append((y, x))

def chk_num(num_map, y, x):
    nums = set(range(1, 10))
    
    # 가로
    nums -= set(num_map[y])
    
    # 세로
    nums -= set(num_map[i][x] for i in range(9))
    
    # 3x3 영역
    area_y = (y // 3) * 3
    area_x = (x // 3) * 3
    for row in range(area_y, area_y + 3):
        nums -= set(num_map[row][area_x:area_x + 3])
    
    return list(nums)

def fill_num(idx):
    if idx == len(blank_pos):  # 모든 빈칸을 채우면 성공
        return True

    y, x = blank_pos[idx]
    
    for num in chk_num(num_map, y, x):  # 가능한 숫자 확인
        num_map[y][x] = num
        if fill_num(idx + 1):  # 다음 빈칸으로 이동
            return True
        num_map[y][x] = 0  # 되돌리기

    return False

# 스도쿠 풀이 실행
fill_num(0)

# 결과 출력
for row in num_map:
    print(*row, sep='')
