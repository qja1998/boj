N = int(input())

x1, y1 = map(int, input().split())
px, py = x1, y1

area = 0
for _ in range(N-1):
    x, y = map(int, input().split())

    area += px * y - x * py

    px, py = x, y

area += px * y1 - x1 * py

area = abs(area) / 2 

print(area)