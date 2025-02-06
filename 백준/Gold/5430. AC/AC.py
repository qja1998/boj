import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    
    
    input_s = input()[1:-2]

    if not n:
        nums = []
    else:
        nums = list(map(int, input_s.split(',')))

    error = False

    is_rev = False
    l, r = 0, n

    for c in p:
        if c == 'R':
            is_rev = not is_rev
        elif c == 'D':
            if l >= r:
                print('error\n')
                error = True
                break
            if not is_rev:
                l += 1
            else:
                r -= 1
    
    if error:
        continue

    nums = nums[l:r]
    
    if is_rev:
        nums = nums[::-1]
    
    print('[')
    for num in nums[:-1]:
        print(f"{num}")
        print(',')
    if nums:
        print(f"{nums[-1]}")
    print(']\n')