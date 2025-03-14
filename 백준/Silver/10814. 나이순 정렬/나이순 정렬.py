count = [[] for _ in range(201)]

N = int(input())

for _ in range(N):
    age, name = input().split()
    age = int(age)
    
    count[age].append(name)

for age, names in enumerate(count):
    for name in names:
        print(age, name)