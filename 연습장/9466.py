import sys
<<<<<<< HEAD
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    n = int(input())
    students = [0] + list(map(int, input().split()))

    visited = []
    for student in students:
        if student in visited:
            continue
        start = student
        tmp_visited = [start]
        is_possible = False
        while True:
            n_student = students[student]
            if n_student == start:
                is_possible = True
                break
            if n_student in tmp_visited:
                break
            tmp_visited.append(n_student)
            student = n_student
        if is_possible:
            visited += tmp_visited
    print(f"{n - len(visited[1:])}\n")
=======
sys.setrecursionlimit(20000)


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    number = numbers[x]
    
    if visited[number]:
        if number in cycle:
            result += cycle[cycle.index(number):]
        return
    else:
        dfs(number)


for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N
    result = []
    
    for i in range(1, N+1):
        if not visited[i]:
            cycle = []
            dfs(i)
            
    print(N - len(result))
>>>>>>> 594e150527375a601f1d6cdedde81cb1b0c6826c
