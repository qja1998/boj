from collections import defaultdict

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    n1, n2, e = map(int, input().split())

    graph[n1].append((n2, e))
    graph[n2].append((n1, e))


node_weights = {1: (0, 1)}
visited = set([1])
min_weight, max_weight = 1_000_000, -1_000_000

is_cycle = False
x = 0


def search_weight(graph, cur_node_idx=1, cur_node_weight=0, is_nag=-1):
    global min_weight, max_weight, x, is_cycle
    for n_node_idx, n_edge in graph[cur_node_idx]:
        n_node_weight = n_edge - cur_node_weight
        if n_node_idx in node_weights:
            # 불가능할 경우
            if node_weights[n_node_idx] != (n_node_weight, is_nag):
                old_weights, old_nag = node_weights[n_node_idx]
                if is_nag != old_nag:
                    x = is_nag * (old_weights - n_node_weight) / 2
                    # x는 정수여야 함
                    if x != int(x):
                        return False
                    x = int(x)
                    is_cycle = True
        if n_node_idx in visited:
            continue

        node_weights[n_node_idx] = (n_node_weight, is_nag)

        min_weight, max_weight = min(n_node_weight, min_weight), max(
            n_node_weight, max_weight
        )

        # x 부호 추가해야 함
        # print(
        #     f"{cur_node_idx} ({cur_node_weight}) -({n_edge})-> {n_node_idx} ({n_edge - cur_node_weight})"
        # )
        visited.add(n_node_idx)
        if not search_weight(graph, n_node_idx, n_node_weight, -1 * is_nag):
            return False
    return True


if search_weight(graph):
    print("Yes")

    # print(node_weights)

    if not is_cycle:

        min_cost = float("inf")
        min_cost_x = 0
        for x in range(min_weight, max_weight + 1):
            cost = 0
            for _, (node_weight, is_nag) in node_weights.items():
                cost += abs(is_nag * x + node_weight)

            if min_cost > cost:
                min_cost = cost
                min_cost_x = x

            # print()
            # print(x)

            result = [0] * N
            for node_index, (node_weight, is_nag) in node_weights.items():
                result[node_index - 1] = is_nag * min_cost_x + node_weight

            # print(*result)

            # print(cost)
            # print()

    else:
        min_cost_x = x

    result = [0] * N
    for node_index, (node_weight, is_nag) in node_weights.items():
        result[node_index - 1] = is_nag * min_cost_x + node_weight

    print(*result)

else:
    print("No")
