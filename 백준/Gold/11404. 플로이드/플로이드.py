n = int(input())
m = int(input())
INF = float("inf")

dist_list = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    dist_list[a][b] = min(dist_list[a][b], c)

for i in range(1, n + 1):
    dist_list[i][i] = 0


def floyd():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist_list[i][j] = min(
                    dist_list[i][j], dist_list[i][k] + dist_list[k][j]
                )

    return dist_list


if __name__ == "__main__":
    floyd()
    # print(*dist_list, sep="\n")
    for dist in dist_list[1:]:
        for d in dist[1:]:
            print(d if d != INF else 0, end=" ")
        print()
