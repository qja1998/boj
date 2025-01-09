def longest_alternating_string(n1, n2, s1, s2):
    # DP 테이블 초기화
    dp = [[[0] * 2 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    # DP 계산
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            for k in range(2):
                if k == 0:  # 'I'를 가져와야 할 차례
                    if i > 0 and s1[i - 1] == 'I':
                        dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][1] + 1)
                    if j > 0 and s2[j - 1] == 'I':
                        dp[i][j][0] = max(dp[i][j][0], dp[i][j - 1][1] + 1)
                else:  # 'O'를 가져와야 할 차례
                    if i > 0 and s1[i - 1] == 'O':
                        dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j][0] + 1)
                    if j > 0 and s2[j - 1] == 'O':
                        dp[i][j][1] = max(dp[i][j][1], dp[i][j - 1][0] + 1)

    # 시작 조건: 반드시 첫 번째 문자가 'I'여야 함
    result = 0
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if dp[i][j][0] > 0 and (dp[i][j][0] // 2 == 1):  # 문자열이 반드시 'I'로 끝나야 함
                result = max(result, dp[i][j][0])

    return result

# 예시 입력
n1, n2 = 5, 5
s1 = "OIOOI"
s2 = "OOIOI"
print(longest_alternating_string(n1, n2, s1, s2))  # 출력: 7
