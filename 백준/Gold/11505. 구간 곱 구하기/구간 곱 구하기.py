N, M, K = map(int, input().split())

MOD = 1_000_000_007

nums = [0] + [int(input()) for _ in range(N)]

tree = [1] * (N * 4)

def init_tree(l, r, i=1):
    if l == r:
        tree[i] = nums[l]
        return tree[i]

    mid = (l + r) // 2
    tree[i] = (init_tree(l, mid, i * 2) * init_tree(mid + 1, r, i * 2 + 1)) % MOD
    
    return tree[i]

def update_tree(l, r, target, change, i=1):
    if l == r == target:
        tree[i] = change
        return tree[i]

    if target < l or target > r:
        return tree[i]

    mid = (l + r) // 2

    tree[i] = (update_tree(l, mid, target, change, i * 2) * update_tree(mid + 1, r, target, change, i * 2 + 1)) % MOD
    return tree[i]

def calculate_tree(l, r, start, end, i=1):
    if l > end or r < start:
        return 1
    if l >= start and end >= r:
        return tree[i]

    mid = (l + r) // 2
    return (calculate_tree(l, mid, start, end, i * 2) * calculate_tree(mid + 1, r, start, end, i * 2 + 1)) % MOD

init_tree(1, N)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    # print(tree)
    if a == 1:
        update_tree(1, N, b, c)
    else:
        print(calculate_tree(1, N, b, c))