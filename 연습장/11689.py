n = int(input())

phi = n

for i in range(2, int(n ** 0.5) + 1):
    if n % i:
        continue
    while n % i == 0:
        n //= i
    
    phi *= 1 - 1 / i

if n > 1:
    phi *= 1 - 1 / n

print(int(phi))