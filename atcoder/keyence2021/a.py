N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ab_max = -1
a_max = -1
for i in range(N):
    a_max = max(a_max, a[i])
    ab_max = max(ab_max, b[i]*a_max)
    print(ab_max)





b1 -> max(a1) = b1.a1
b2 -> max(a1 a2) = b2.a2
b3 -> max(a1 a2 a3) = b3.a2