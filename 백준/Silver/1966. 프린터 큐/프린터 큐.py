from collections import deque
import heapq

def nag_int(s):
    """음수 정수를 반환환"""
    return -int(s)

TC = int(input())
for t in range(TC):
    N, M = map(int, input().split())
    importance_list = list(map(nag_int, input().split()))
    q = deque([(i, im) for i, im in enumerate(importance_list)])
    heapq.heapify(importance_list)

    cnt = 1
    cur_min = heapq.heappop(importance_list)

    while q:
        i, im = q.popleft()
        if i == M and cur_min == im:
            # M 번째 출력되면 끝
            break
        elif cur_min == im:
            # 출력 가능하면 다음으로
            cur_min = heapq.heappop(importance_list)
            cnt += 1
        else:
            # 출력 안되면 대기열 맨 뒤로
            q.append((i, im))
    print(cnt)
        