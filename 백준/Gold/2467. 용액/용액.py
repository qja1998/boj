from bisect import bisect_left

N = int(input())

liq_arr = list(map(int, input().split()))

left_idx = 0
right_idx = N - 1

ans = abs(liq_arr[left_idx] + liq_arr[right_idx])
ans_left = left_idx
ans_right = right_idx

while left_idx < right_idx: # left_idx와 right_idx는 만나면 안된다
    tmp = liq_arr[left_idx] + liq_arr[right_idx]

    if abs(tmp) < ans:
        ans_left = left_idx
        ans_right = right_idx
        ans = abs(tmp)

        if ans == 0:
            break
    
    if tmp < 0:
        left_idx += 1
    
    else:
        right_idx -= 1

print(liq_arr[ans_left], liq_arr[ans_right])