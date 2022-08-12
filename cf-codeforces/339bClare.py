houses, number_of_tasks = map(int, input().split())
tasks = list(map(int, input().split()))

 
distance = 0
if tasks[0] > 1:
        distance = tasks[0] - 1
for i in range(len(tasks) - 1):
    if tasks[i] > tasks [i+1]:
        distance += houses - tasks[i] + tasks[i+1]
    else:
        distance += tasks[i+1] - tasks[i]
print(distance)