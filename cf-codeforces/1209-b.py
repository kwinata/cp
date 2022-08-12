from collections import defaultdict
from typing import List


class LampStatus:
    OFF = '0'
    ON = '1'

    @staticmethod
    def flip(status):
        if status == LampStatus.ON:
            return LampStatus.OFF
        elif status == LampStatus.OFF:
            return LampStatus.ON
        else:
            raise ValueError()


class Lamp:
    def __init__(self, interval, start, status):
        self.interval = interval
        self.start = start
        self.status = status

    def execute_time(self, t):
        if t >= self.start and (t-self.start) % self.interval == 0:
            self.status = LampStatus.flip(self.status)


def koala(lamps: List[Lamp]):
    current_max = 0
    for i in range(300):
        for lamp in lamps:
            lamp.execute_time(i)
        lamps_on = len(list(filter(lambda l: l.status == LampStatus.ON, lamps)))
        current_max = max(current_max, lamps_on)
    return current_max


if __name__ == "__main__":
    n = int(input())
    status = input()
    lamps = []
    for i in range(n):
        ai, bi = map(int, input().split())
        lamps.append(Lamp(ai, bi, status[i]))
    print(koala(lamps))
