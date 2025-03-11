def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b, gcd_num):
    i = b
    while True:
        if i % a == 0 and i % b == 0:
            return i
        i += gcd_num

a, b = map(int, input().split())
if a < b :
    a, b = a, b

gcd_num = gcd(a, b)
print(gcd_num)
print(lcm(a, b, gcd_num))