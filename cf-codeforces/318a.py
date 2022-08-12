import math
number, position = map(int, input().split())

 
if position <= math.ceil(number / 2):
    print(int(position)*2 - 1)
else:
    print(int(position - number / 2)*2)


