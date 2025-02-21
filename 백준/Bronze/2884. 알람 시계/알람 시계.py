h, m = map(int, input().split())
m -= 45

if m >= 0:
    print(h, m)
else:
    h -= 1
    m += 60
    if h >= 0:
        print(h, m)
    else:
        print(h + 24, m)