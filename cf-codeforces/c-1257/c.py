from collections import Counter


def dominated(x, arr, memory):
    if x < 2:
        return False
    for i in range(len(arr) - x + 1):
        if (i, i+x-2) in memory:
            col = memory[(i, i+x-2)]
            if arr[i+x-1] in col:
                col[arr[i+x-1]] += 1
            else:
                col[arr[i+x-1]] = 1
        else:
            arr_ = arr[i:i + x]
            col = Counter(arr_)
        memory[(i, i+x-1)] = col
        occurrences = list(dict(col).values())
        occurrences.sort()
        if len(occurrences) == 1 or occurrences[-1] != occurrences[-2]:
            return True
    return False


def test_dominated():
    assert dominated(6, [1, 2, 3, 4, 5, 1])
    assert not dominated(3, [1, 2, 3, 4, 5, 1])
    assert not dominated(4, [1, 2, 3, 4, 5, 1])
    assert dominated(2, [3, 3, 3, 3])
    assert dominated(5, [1, 3, 2, 3, 4, 5, 2])


def bin_search(arr):
    memory = {}
    for i in range(2, len(arr) + 1):
        if dominated(i, arr, memory):
            return i
    return -1


def test_search():
    assert bin_search([3, 3, 3, 3]) == 2
    assert bin_search([1, 2, 3, 4, 5, 1]) == 6


def test_time():
    assert bin_search([1, 2, 3, 4, 5, 6, 1]) == 7
    assert bin_search([i for i in range(1, int(1e3))] + [1]) == 1000
    # assert bin_search([i for i in range(1, int(1e5))] + [1])


if __name__ == "__main__":
    t = int(input())
    for __ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        if len(arr) < 2:
            print(-1)
            continue
        print(bin_search(arr))
