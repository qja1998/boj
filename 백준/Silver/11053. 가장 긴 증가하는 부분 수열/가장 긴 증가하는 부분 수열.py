from bisect import bisect_left

N = int(input())

A = list(map(int, input().split()))

result = [A[0]]

for num in A[1:]:
    if result[-1] < num:
        result.append(num)
    else:
        i = bisect_left(result, num)
        result[i] = num

print(len(result))