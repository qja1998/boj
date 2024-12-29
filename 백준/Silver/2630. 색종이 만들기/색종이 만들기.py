N = int(input())

paper = []
for _ in range(N):
    paper.append(list(map(int, input().split(' '))))


blue = 0
white = 0
def quard_tree(i, j, n, paper):
    global blue, white
    default_color = paper[i][j]
    for _i in range(i, i + n):
        for _j in range(j, j + n):
            if paper[_i][_j] != default_color:
                quard_tree(i,          j,          n // 2, paper)
                quard_tree(i + n // 2, j,          n // 2, paper)
                quard_tree(i,          j + n // 2, n // 2, paper)
                quard_tree(i + n // 2, j + n // 2, n // 2, paper)
                return
    if default_color:
        blue += 1
    else:
        white += 1
    return

quard_tree(0, 0, N, paper)

print(white)
print(blue)