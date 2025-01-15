n=int(input())
ans = n

for i in range(2, int(n**0.5)+1):
    # i로 나누어 떨어진다면
    if n % i == 0:
        # n이 가지고 있는 i의 개수 만큼 나눠주기
        while n % i == 0:   
            n //= i
        # 오일러 피 함수 
        ans *= (1-1/i)

# 자기 자신이 소수였던 경우
if n>1:
    ans *= (1-1/n)

print(int(ans))