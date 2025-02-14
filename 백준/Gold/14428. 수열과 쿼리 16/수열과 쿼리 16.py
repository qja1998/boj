INF = float('inf')

N = int(input())

nums = [0] + list(map(int, input().split()))

tree = [[1, 1] for _ in range((N * 4))]

def print_tree():
    i = 1
    d = 0
    while i < N * 4:
        print(tree[i:i + 2 ** d])
        d += 1
        i *= 2

def init_tree(l, r, i=1):
    if l == r:
        tree[i] = [nums[l], l]
        return tree[i]

    mid = (l + r) // 2
    tree[i] = min(init_tree(l, mid, i * 2), init_tree(mid + 1, r, i * 2 + 1))
    
    return tree[i]

def update_tree(l, r, target, change, i=1):
    if l == r == target:
        # print('find', l, r, target)
        tree[i] = [change, target]
        # print(tree[i],  change)
        return tree[i]

    if target < l or target > r:
        return tree[i]

    mid = (l + r) // 2
    # print(i)
    tree[i] = min(update_tree(l, mid, target, change, i * 2), update_tree(mid + 1, r, target, change, i * 2 + 1))
    # print(i, tree[i])
    return tree[i]

def calculate_tree(l, r, start, end, i=1):
    if l > end or r < start:
        return [INF, INF]
    
    if l >= start and end >= r:
        return tree[i]

    mid = (l + r) // 2
    return min(calculate_tree(l, mid, start, end, i * 2), calculate_tree(mid + 1, r, start, end, i * 2 + 1))

init_tree(1, N)

M = int(input())

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        update_tree(1, N, b, c)
        # print_tree()
    else:
        print(calculate_tree(1, N, b, c)[1])