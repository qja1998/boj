import sys
n = int(sys.stdin.readline().rstrip())
result = 0
zero = False
nag = []
pos = []
for _ in range(n):
    tmp = int(sys.stdin.readline().rstrip())
    if tmp < 0:
        nag.append(tmp)
    elif tmp >1:
        pos.append(tmp)
    elif tmp == 0 and not zero:
        zero = True
    elif tmp == 1:
        result += 1

def counting_sort(array, max):
    counting_array = [0]*(max+1)
    for i in array:
        counting_array[i] += 1
 
    for i in range(max):
        counting_array[i+1] += counting_array[i]
 
    output_array = [-1]*len(array)
    
    for i in array:
        output_array[counting_array[i] -1] = i
        counting_array[i] -= 1
    return output_array

if nag:
    nag = counting_sort(nag, -min(nag))
if pos:
    pos = counting_sort(pos, max(pos))
if zero:
    nag.append(0)
lng = len(pos)
sht = len(nag)
if lng > sht:
    i = 0
    while i < sht:
        rev = -i - 1
        if i != sht- 1:
            result += nag[i] * nag[i + 1] + pos[rev] * pos[rev - 1]
            i += 1
        else:
            result += nag[i] + pos[rev] * pos[rev - 1]
            i += 1
        i += 1
    while i < lng:
        rev = -i - 1
        if i != lng- 1:
            result += pos[rev] * pos[rev - 1]
            i += 1
        else:
            result += pos[rev]
        i += 1
elif lng < sht:
    lng, sht = sht, lng
    i = 0
    while i < sht:
        rev = -i - 1
        if i != sht- 1:
            result += nag[i] * nag[i + 1] + pos[rev] * pos[rev - 1]
            i += 1
        else:
            result += pos[rev] + nag[i] * nag[i + 1]
            i += 1
        i += 1
    while i < lng:
        if i != lng- 1:
            result += nag[i] * nag[i + 1]
            i += 1
        else:
            result += nag[i]
        i += 1
        
else:
    i = 0
    while i < sht:
        rev = -i - 1
        if i != sht- 1:
            result += nag[i] * nag[i + 1] + pos[rev] * pos[rev - 1]
            i += 1
        else:
            result += nag[i] + pos[rev]
        i += 1
print(result)