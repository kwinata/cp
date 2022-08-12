numbers = list(map(int, input().split('+')))
for _ in range(len(numbers) - 1):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp      
equation = ''

for number in numbers:
    equation += str(number)+'+'

print(equation[:-1])