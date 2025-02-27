N = int(input())

max_h = 0
pillar_list = [0] * 1001

max_loc = 0
for _ in range(N):
    loc, h = map(int, input().split())
    max_h = max(max_h, h)
    max_loc = max(max_loc, loc)
    pillar_list[loc] = h

# print(pillar_list)
# 왼쪽에서 시작
i_l = -1
cur = 0
ans = 0
while cur < max_h:
    i_l += 1
    cur = max(cur, pillar_list[i_l])
    # print(cur)
    ans += cur
i_r = max_loc + 1
cur = 0
while cur < max_h:
    i_r -= 1
    cur = max(cur, pillar_list[i_r])
    # print(cur)
    ans += cur
# print(i_l, i_r)

if i_r == i_l:
    ans -= max_h
else:
    ans += max_h * (i_r - i_l - 1)

print(ans)