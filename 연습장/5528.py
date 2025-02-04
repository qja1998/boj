'''import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# train_list[0] = S열차 (뒤집어서 [::-1]했던 것 유지), train_list[1] = T열차
train_list = [list(input().strip())[::-1] for _ in range(2)]

# dp_prev[t][0 or 1]: "이전 행(s-1)"에서 T의 t번째까지 고려했을 때 dp값
# dp_curr[t][0 or 1]: "현재 행(s)"에서 T의 t번째까지 고려했을 때 dp값
dp_prev = [[1, 1] for _ in range(M)]
dp_curr = [[1, 1] for _ in range(M)]

ans = 0

for s in range(N):
    # 이번에 s가 1 증가했으므로, 이전 단계의 정보를 dp_prev로 삼고
    # dp_curr를 "덮어쓰기" 방식으로 사용
    dp_prev, dp_curr = dp_curr, dp_prev

    for t in range(M):

        # 먼저 dp_curr[t][i]를 1로 초기화
        dp_curr[t][0] = 1
        dp_curr[t][1] = 1

        # ===== S에서 뽑는 경우 =====
        cur = train_list[0][s]  # 현재 뽑으려는 칸
        tmp_res = 1

        if s > 0 and train_list[0][s - 1] != cur:
            tmp_res = max(tmp_res, dp_prev[t][0] + 1)

        if t > 0 and train_list[1][t - 1] != cur:
            tmp_res = max(tmp_res, dp_curr[t - 1][1] + 1)

        dp_curr[t][0] = tmp_res
        if tmp_res % 2 == 1 and tmp_res > ans:
            ans = tmp_res

        # ===== T에서 뽑는 경우 =====
        cur = train_list[1][t]
        tmp_res = 1

        if s > 0 and train_list[0][s - 1] != cur:
            tmp_res = max(tmp_res, dp_prev[t][0] + 1)

        if t > 0 and train_list[1][t - 1] != cur:
            tmp_res = max(tmp_res, dp_curr[t - 1][1] + 1)

        dp_curr[t][1] = tmp_res
        if tmp_res % 2 == 1 and tmp_res > ans:
            ans = tmp_res

print(ans)
'''

INF = float('inf')
def main():
    import sys
    N, M = map(int, input().split())
    # train_list[0] = S열차 (뒤집어서 [::-1]했던 것 유지), train_list[1] = T열차
    
    S = list(input().strip())
    T = list(input().strip())

    # I -> 0, O -> 1 로 변환
    S = [0 if char == 'I' else 1 for char in S]
    T = [0 if char == 'I' else 1 for char in T]

    # 2차원 배열로 롤링
    prev_dp = [[0, 0] for _ in range(N + 1)]
    curr_dp = [[0, 0] for _ in range(N + 1)]

    # 초기값: 모든 dp[s][t][0] = -∞, dp[s][t][1] = 0
    for t in range(N + 1):
        prev_dp[t][0] = -INF

    # DP 점화식 계산
    for s in range(M + 1):
        for t in range(N + 1):
            # 초기화
            curr_dp[t][0] = -INF
            curr_dp[t][1] = 0

            if s > 0:
                curr_dp[t][S[s - 1]] = max(curr_dp[t][S[s - 1]], prev_dp[t][1 - S[s - 1]] + 1)
            if t > 0:
                curr_dp[t][T[t - 1]] = max(curr_dp[t][T[t - 1]], curr_dp[t - 1][1 - T[t - 1]] + 1)

        # 현재 dp를 이전 dp로 교체
        prev_dp, curr_dp = curr_dp, prev_dp

    # 결과 계산
    res = 0
    for t in range(N + 1):
        res = max(res, prev_dp[t][0])

    print(res)


if __name__ == "__main__":
    main()