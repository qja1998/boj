import sys
N, M, K = map(int, sys.stdin.readline().split())

# 세그먼트 트리 구성
def build(n):
    p = 0
    m = 0
    # n보다 크면서 가장 가까운 제곱수
    while n > m:
        m = 2 ** p
        p += 1
    tree = [0] * (m * 2)

    # 리프 노드는 입력된 원래 값
    for i in range(N):
        tree[i + m] = int(sys.stdin.readline())
    # 부모 노드를 자식의 합으로 만들기기
    for i in range(m - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[(2 * i) + 1]
    return tree, m
    
tree, leaf = build(N)

def update(tree, b, c, leaf):
    idx = leaf + b - 1
    diff = c - tree[idx]
    # 부모로 거슬러 올라가면서 업데이트
    while idx:
        tree[idx] += diff
        idx //= 2
    return tree
    
def interval_sum(tree, b, c, leaf):
    total = []
    start = leaf + b - 1
    end = leaf + c - 1
    while start < end:
        if start % 2:
            total.append(tree[start])
        start = (start + 1) // 2
        if not end % 2:
            total.append(tree[end])
        end = (end - 1) // 2
    if start == end:
        total.append(tree[start])
    return sum(total)
    
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        tree = update(tree, b, c, leaf)
    else:
        answer = interval_sum(tree, b, c, leaf)
        print(answer)