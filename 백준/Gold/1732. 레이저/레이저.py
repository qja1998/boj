N = int(input())
degree = {}
ans = set()
for _ in range(N):
    x,y,d = map(int,input().split())
    if x == 0: deg = 'x_zero'
    elif y==0:
        if x >0: deg = 'plus_zero'
        else: deg = 'minus_zero'
    else: deg = y/x
    if deg not in degree:
        degree[deg] = []
    degree[deg].append([abs(x)+abs(y),x,y,d])

for value in degree.values():
    if len(value) == 1: continue
    arr = value
    arr.sort()
    max_height = -1
    for temp in arr:
        if max_height < temp[3]:
            max_height = temp[3]
        else:
            ans.add((temp[1],temp[2]))

answer = list(ans)
answer.sort()
# print(degree)
for i in answer:
    print(*i)