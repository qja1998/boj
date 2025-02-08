N = int(input())

for _ in range(N):
    s = input()

    total_score = 0
    score = 0
    for c in s:
        if c == 'O':
            score += 1
        else:
            score = 0
        total_score += score
    print(total_score)