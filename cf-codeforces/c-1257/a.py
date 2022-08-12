t = int(input())
for __ in range(t):
    n, x, a, b = map(int, input().split())
    cur_dis = abs(a-b)
    print(min(n-1, cur_dis+x))