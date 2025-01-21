#include <stdio.h>
#include <string.h>

#define MAX_M 2048
#define MAX_N 2048
#define INF -1001001001

// chmax 함수 정의
int chmax(int t, int f) {
    return (t > f) ? t : f;
}

int main() {
    int M, N;
    char S[MAX_M + 1], T[MAX_N + 1];
    int dp[MAX_M + 1][MAX_N + 1][2];

    // 입력 받기
    scanf("%d %d", &M, &N);
    scanf("%s", S);
    scanf("%s", T);

    // I -> 0, O -> 1로 변환
    for (int i = 0; i < M; i++) {
        S[i] = (S[i] == 'I') ? 0 : 1;
    }
    for (int i = 0; i < N; i++) {
        T[i] = (T[i] == 'I') ? 0 : 1;
    }

    // dp 배열 초기화
    for (int i = 0; i <= M; i++) {
        for (int j = 0; j <= N; j++) {
            dp[i][j][0] = INF;
            dp[i][j][1] = 0;
        }
    }

    // DP 점화식 계산
    for (int s = 0; s <= M; s++) {
        for (int t = 0; t <= N; t++) {
            if (s < M) {
                dp[s + 1][t][S[s]] = chmax(dp[s + 1][t][S[s]], dp[s][t][1 - S[s]] + 1);
            }
            if (t < N) {
                dp[s][t + 1][T[t]] = chmax(dp[s][t + 1][T[t]], dp[s][t][1 - T[t]] + 1);
            }
        }
    }

    // 결과 계산
    int res = 0;
    for (int s = 0; s <= M; s++) {
        for (int t = 0; t <= N; t++) {
            res = chmax(res, dp[s][t][0]);
        }
    }

    // 결과 출력
    printf("%d\n", res);

    return 0;
}
