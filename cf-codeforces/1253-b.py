class Day:
    def __init__(self):
        self.office = set()
        self.events = 0
        self.signed_in = set()

    def sign_in(self, eid):
        if eid in self.office:
            raise ValueError()
        if eid in self.signed_in:
            raise ValueError()
        self.office.add(eid)
        self.signed_in.add(eid)
        self.events += 1

    def sign_out(self, eid):
        if eid not in self.office:
            raise ValueError()
        self.office.remove(eid)
        self.events += 1

    def is_end_of_day(self):
        if len(self.office) == 0:
            return self.events
        else:
            return None

    def flush(self):
        self.events = 0
        self.office = set()
        self.signed_in = set()


def silly_mistake(events):
    day = Day()
    days = []
    for event in events:
        try:
            if event > 0:
                day.sign_in(event)
            else:
                day.sign_out(-event)
        except ValueError:
            return [-1]
        if day.is_end_of_day():
            days.append(day.is_end_of_day())
            day.flush()
    if day.is_end_of_day() is None:
        return [-1]
    return days


def test():
    assert [6] == silly_mistake([1, 7, -7, 3, -1, -3])
    assert [-1] == silly_mistake([1, -1, 2, 3])


if __name__ == "__main__":
    __ = input()
    array = list(map(int, input().split()))
    days = silly_mistake(array)
    if days != [-1]:
        print(len(days))
    print(" ".join(map(str, days)))
