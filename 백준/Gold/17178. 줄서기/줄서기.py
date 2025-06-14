from collections import deque, defaultdict

N = int(input())


def perprocess(s):
    alpha, digit = s.split("-")
    return alpha, int(digit)


lines = []
for _ in range(N):
    lines += list(map(perprocess, input().split()))

order = sorted(lines)
lines = deque(lines)
# stack을 활용해서 정렬 가능한가

waiting_line = []
chk_dict = defaultdict(bool)
order_idx = 0

result = "BAD"
# print(lines)
# print(order)
while lines:
    # 차례 확인
    cur_order = order[order_idx]
    # 차례의 티켓이 들어올 때까지 반복
    if not chk_dict[cur_order]:
        cur = lines.popleft()
        # 대기열 이동
        waiting_line.append(cur)
        chk_dict[cur] = True
        continue
    # 해당 차례 번호가 이미 대기열에 있음
    # print(waiting_line, cur_order)
    # 대기열 맨 앞에 없음
    if waiting_line.pop() != cur_order:
        break
    order_idx += 1
else:
    # print(waiting_line[::-1], order[order_idx:])
    if waiting_line[::-1] == order[order_idx:]:
        result = "GOOD"

print(result)
