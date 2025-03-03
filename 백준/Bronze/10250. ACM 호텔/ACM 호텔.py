# YXX, YYXX

# 엘베는 이동 거리 포함 안됨
# 같은 거리면 낮은 층수

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    floor = N % H
    n = N // H + 1
    if floor == 0:
        floor += H
        n -= 1
    if n < 10:
        print(f"{floor}0{n}")
    else:
        print(f"{floor}{n}")