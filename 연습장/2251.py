bottle_list = list(map(int, input().split()))

water_list = [0, 0, bottle_list[2]]

def move_water(i, j, b2):
    '''
    b: 물병의 용량
    '''
    print()
    print(water_list)
    w1, w2 = water_list[i], water_list[j]
    remain_b = b2 - w2
    print(w1, '->', w2)
    # 옮길 물의 양이 더 많은 경우
    if w1 > remain_b:
        w1 -= remain_b
        w2 += remain_b
    else:
        w2 += w1
        w1 = 0

    water_list[i], water_list[j] = w1, w2
    print(water_list)
    print()
    return water_list

result = []
visited = []

def dfs(water_list, pre_move=(-1, -1), visited=[]):
    '''
    가득 찬 물병에는 옮길 수 없음
    직전 이동의 반대는 생략
    같은 조합은 visited 처리
    
    첫 번째 물통이 비어있을 경우 return
    -> 어차피 조합 다 보면 끝남
    '''
    for i, w1 in enumerate(water_list):
        for j, w2 in enumerate(water_list):
            if i == j:
                continue
            
            # w1 -> w2
            pre_water = water_list[:]
            water_list = move_water(i, j, bottle_list[j])
            
            # 이미 해봤던 조합 생략
            if water_list in visited:
                continue
            
            # 첫 번째 물통이 비었으면 기록
            if water_list[0] == 0:
                # print('find:', water_list)
                result.append(water_list[2])
            dfs(water_list, (i, j), visited + [water_list[:]])
            
            # 원래대로
            water_list = pre_water

dfs(water_list)

print(*sorted(result), sep=' ')