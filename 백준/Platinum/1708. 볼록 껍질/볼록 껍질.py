def diff(a, b):
    return b[0] - a[0], b[1] - a[1]

def is_ccw(a, b, c):
    v1 = diff(a, b)
    v2 = diff(b, c)
    return v1[0] * v2[1] > v1[1] * v2[0]

def hull(points):
    stack = []
    for pt in points:
        while len(stack) >= 2 and not is_ccw(stack[-2], stack[-1], pt):
            stack.pop()
        stack.append(pt)
    return len(stack)

n = int(input())
pts = [tuple(map(int, input().split())) for _ in range(n)]
pts.sort()

res = -2
res += hull(pts)
res += hull(pts[::-1])

print(res)
