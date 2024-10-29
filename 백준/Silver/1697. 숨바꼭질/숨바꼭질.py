from collections import deque

def solution(N, K):
    q = deque([(N, 0)])
    visited = set([N])

    if N == K:
        return 0

    while q:
        cur_pos, time = q.popleft()
        if cur_pos > K:
            n_pos_list = [cur_pos - 1]
        else:
            n_pos_list = [cur_pos + 1, cur_pos - 1, cur_pos * 2]

        for n_pos in n_pos_list:
            if n_pos < 0:
                continue
            if n_pos in visited:
                continue
            if n_pos == K:
                return time+1
            q.append((n_pos, time+1))
            visited.add(n_pos)

if __name__ == '__main__':
    N, K = map(int, input().split())
    print(solution(N, K))