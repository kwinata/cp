from typing import Tuple, List


def read_input() -> Tuple[int, List[int]]:
    n, m = (int(i) for i in input().split())
    return n, [int(i)-1 for i in input().split()]


def run_through(n: int, likes: List[int]):
    position_of_post = [i for i in range(n)]
    post_at_position = [i for i in range(n)]

    history = [{'max': i, 'min': i} for i in range(n)]
    for liked in likes:
        position_of_liked = position_of_post[liked]
        if position_of_liked == 0:
            continue
        victim = post_at_position[position_of_liked-1]
        position_of_post[liked] -= 1
        position_of_post[victim] += 1
        post_at_position[position_of_liked], post_at_position[position_of_liked-1] = \
            post_at_position[position_of_liked-1], post_at_position[position_of_liked]
        history[liked]['min'] = min(position_of_post[liked], history[liked]['min'])
        history[victim]['max'] = max(position_of_post[victim], history[victim]['max'])

    return history


if __name__ == "__main__":
    n, likes = read_input()
    history = run_through(n, likes)
    for post in history:
        print(post['min']+1, post['max']+1)
