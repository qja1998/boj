n = int(input())
A = [0]*n

for i in range(n):
    A[i] = list(map(int,input().split()))
    
for i in range(1,n):
    A[i][0]= min(A[i-1][1], A[i-1][2]) + A[i][0]
    A[i][1]= min(A[i-1][0], A[i-1][2]) + A[i][1]
    A[i][2]= min(A[i-1][0], A[i-1][1]) + A[i][2]

print(min(A[n-1][0],A[n-1][1],A[n-1][2]))