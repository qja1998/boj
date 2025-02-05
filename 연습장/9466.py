import sys
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