import heapq
from collections import defaultdict

N = int(input())
tree = defaultdict(list)
visited = defaultdict(bool)

start_list = set()

ant_foods = []
for _ in range(N):
    _, *foods = input().split()
    heapq.heappush(ant_foods, foods)

while ant_foods:
    foods = heapq.heappop(ant_foods)

    for i, food in enumerate(foods):
        # print(food)
        if visited[(tuple(foods[:i]), food, i)]:
            continue
        print(i * '--' + food)
        visited[(tuple(foods[:i]), food, i)] = True