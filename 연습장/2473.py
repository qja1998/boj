N = int(input())

liq_list = sorted(list(map(int, input().split())))

min_val = float('inf')
liq_res = [0, 1, 2]

done = False
for i in range(N-2):
    cur_fix = liq_list[i]

    l, r = i + 1, N - 1

    while l < r:
        cur = cur_fix + liq_list[l] + liq_list[r]

        if abs(min_val) > abs(cur):
            min_val = cur
            liq_res = [i, l, r]
        
        if cur < 0:
            l += 1
        elif cur > 0:
            r -= 1
        else:
            done = True
            break
    if done:
        break
    
print(liq_list[liq_res[0]], liq_list[liq_res[1]], liq_list[liq_res[2]])