import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
bucket_size = int(N**.5)
min_bucket = [1_000_000_000 for _ in range(N//bucket_size + 1)]
max_bucket = [0 for _ in range(N//bucket_size + 1)]
# 초기화
for i in range(N):
    min_bucket[i//bucket_size] = min(min_bucket[i//bucket_size], A[i])
    max_bucket[i//bucket_size] = max(max_bucket[i//bucket_size], A[i])
def query(l, r):
    M, m = 0, 1_000_000_000
    left_bucket_num, right_bucket_num = l//bucket_size, r//bucket_size
    for i in range(left_bucket_num+1, right_bucket_num):
        M = max(M, max_bucket[i])
        m = min(m, min_bucket[i])
    if left_bucket_num == right_bucket_num:
        for i in range(l, r+1):
            M = max(M, A[i])
            m = min(m, A[i])
    else:
        for i in range(l, (left_bucket_num+1)*bucket_size):
            M = max(M, A[i])
            m = min(m, A[i])
        for i in range(right_bucket_num*bucket_size, r+1):
            M = max(M, A[i])
            m = min(m, A[i])
    return m, M
ans = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(*query(a, b))