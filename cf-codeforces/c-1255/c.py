from collections import defaultdict





def build_hash(triplets):
    q_map = defaultdict(list)
    for triplet in triplets:
        for q in triplet:
            q_map[q].append(tuple(triplet))
    return q_map


def find_one_end(q_map):
    for q, triplets in q_map.items():
        if len(triplets) == 1:
            return q, triplets[0]


def find_second(first_value, q_map):
    for q, triplets in q_map.items():
        if len(triplets) == 2:
            for triplet in triplets:
                if first_value in triplet:
                    return q, triplet


def remove(q_map, triplet):
    q_map[triplet[0]].remove(triplet)
    q_map[triplet[1]].remove(triplet)
    q_map[triplet[2]].remove(triplet)


def fill_next(ps, q_map):
    left = set(q_map[ps[-1]])
    right = set(q_map[ps[-2]])
    triplets = list(left.intersection(right))
    triplet = triplets[0]
    value = [i for i in triplet if i not in ps[-2:]][0]
    ps.append(value)
    remove(q_map, triplet)


def construct(q_map, n):
    first, first_triplet = find_one_end(q_map)
    second, second_triplet = find_second(first, q_map)
    ps = [first, second]
    while len(ps) < n:
        fill_next(ps, q_map)
    return ps


inp = Input()
n = int(inp.input())
triplets = []
for i in range(n-2):
    triplets.append(inp.input_int_list())
ps = construct(build_hash(triplets), n)
print(" ".join(map(str, ps)))
