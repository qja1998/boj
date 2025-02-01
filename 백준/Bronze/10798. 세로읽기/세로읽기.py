sero_list = ['' for _ in range(15)]

while True:
    try:
        s = input()
        for i, c in enumerate(s):
            sero_list[i] += c
    except:
        break

print(*sero_list, sep='')
