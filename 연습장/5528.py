N,M=map(int,input().split())
S=input()
T=input()
DP=[[0,-1]for _ in range(M+1)]
ans=0
for i in range(N+1):
  for j in range(M+1):
    if i>0:
      if S[i-1]=='I':
        DP[j][1]=DP[j][0]+1
        DP[j][0]=0
      else:
        DP[j][0]=DP[j][1]+1
        DP[j][1]=-1
    if j>0:
      if T[j-1]=='I':
        DP[j][1]=max(DP[j][1],DP[j-1][0]+1)
      else:
        DP[j][0]=max(DP[j][0],DP[j-1][1]+1)
    ans=max(ans,max(DP[j]))
if ans>0 and ans%2==0:ans-=1

print(DP)
print(ans)