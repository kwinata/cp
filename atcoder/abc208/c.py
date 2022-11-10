N, K = map(int, input().split())
id = list(map(int, input().split()))
length = len(id)
remaining = K % length
# candies = [K//length] * length
id_min = set(sorted(id)[0:remaining])
for i in range(length):
    if id[i] in id_min:
        print(K//length + 1)
    else:
        print(K//length)
