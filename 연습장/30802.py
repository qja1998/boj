N = int(input())

shirts = list(map(int, input().split()))

T, P = map(int, input().split())

s = 0
for shirt in shirts:
    if shirt == 0:
        continue
    if shirt % T == 0:
        s += shirt // T
    else:
        s += shirt // T + 1


pans = sum(shirts)
p, p_m = pans // P, pans % P

print(s)
print(p, p_m)