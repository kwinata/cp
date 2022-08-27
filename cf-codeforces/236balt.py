import math
a, b, c = map(int, input().split())
 
sum = 0
modulo = 1073741824 * pow(2, 30)
def factors(number):
    if number == 1:
        counter = 1
        return counter
    counter = 2
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            if i*i == number:
                counter += 1
            else:
            	counter += 2
    return counter
 
from collections import defaultdict
# print(factors(1))
factor = defaultdict(int)
 
from tqdm import tqdm
for a in tqdm(range(1, a+1)):
    for b in range(1, b+1):
        for c in range(1, c+1):
            multiplication = a * b * c
            if multiplication not in factor:
                factor[multiplication] = factors(multiplication)
            sum += factor[multiplication]
            sum %= modulo
 
print(sum)