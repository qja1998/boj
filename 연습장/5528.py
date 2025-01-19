N, M = map(int, input().split())

train_list = [list(input()) for _ in range(2)]

# dp[s][t][i] = S의 s번째, T의 t번째까지 선택했을 때, train_list[i] 선택 시의 최대 길이
dp = [[[1, 1] for _ in range(M)] for _ in range(N)]

ans = 0
for s in range(N):
    for t in range(M):
        # 두 열차 중 하나를 고름
        for i in range(2):
            tmp_res = 1
            cur = train_list[i][s if i == 0 else t]
            # 이전에 S에서 연결했고 현재 열차가 연결이 가능할 때
            if s > 0 and train_list[0][s - 1] != cur:
                tmp_res = max(tmp_res, dp[s - 1][t][0] + 1)
            elif s > 0:
                tmp_res = max(tmp_res, dp[s - 1][t][0])

            # 이전에 T에서 연결했고 현재 열차가 연결이 가능할 때
            if t > 0 and train_list[1][t - 1] != cur:
                tmp_res = max(tmp_res, dp[s][t - 1][1] + 1)
            elif t > 0:
                tmp_res = max(tmp_res, dp[s][t - 1][1])
            
            dp[s][t][i] = tmp_res
            ans = max(ans, tmp_res)

print(*dp, sep='\n')
print(ans)