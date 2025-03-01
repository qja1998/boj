def makeLps(p): #Lps 배열을 만든 후 리턴
    tmpTable = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = tmpTable[j - 1]
        if p[i] == p[j]:
            j += 1
            tmpTable[i] = j
    return tmpTable
 
def KMP(T, P):
    result = []
    cnt = 0
    
    j = 0
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = table[j - 1]
        
        if T[i] == P[j]:
            if j == len(P) - 1: #패턴과 모두 일치할 경우
                cnt += 1
                result.append(i - len(P) + 2)
                j = table[j]
            else:
                j += 1
    return cnt, result
    
    
 
T = input()
P = input()
 
table = makeLps(P)
 
a, b = KMP(T, P)
print(a)
print(*b)