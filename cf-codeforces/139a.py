pages = int(input())
pages_read = list(map(int, input().split()))

day_tracker = -1
while pages > 0:
    day_tracker += 1
    day_tracker %= 7
    pages -= pages_read[day_tracker]
print(day_tracker+1)