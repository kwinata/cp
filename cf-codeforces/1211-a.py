class SetWithHistory:
    def __init__(self):
        self.members = set()
        self.step = 0
        self.important_history = []

    def add(self, mid):
        self.step += 1
        if mid not in self.members:
            self.members.add(mid)
            self.important_history.append([mid, self.step])

    def get_abc(self):
        sorted_history = sorted(self.important_history, key=lambda x: x[0])
        return (history[1] for history in sorted_history)


if __name__ == "__main__":
    __ = input()
    swh = SetWithHistory()
    rs = list(map(int, input().split()))
    for r in rs:
        swh.add(r)
        if len(swh.members) >= 3:
            print(" ".join(map(str, swh.get_abc())))
            exit(0)
    print("-1 -1 -1")
