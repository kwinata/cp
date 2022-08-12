from typing import List


def get_least_total(n, row_1: List[int], row_2: List[int], cross: List[int]):
    current_distance = cross[0] + sum(row_2)
    distances = [current_distance]
    for i in range(1, n):
        current_distance -= row_2[i-1]
        current_distance -= cross[i-1]
        current_distance += row_1[i-1]
        current_distance += cross[i]
        distances.append(current_distance)
    distances = sorted(distances)
    return distances[0] + distances[1]


n = int(input())
row1 = [int(i) for i in input().split()]
row2 = [int(i) for i in input().split()]
cross_prices = [int(i) for i in input().split()]
print(get_least_total(n, row1, row2, cross_prices))
