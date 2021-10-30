n = int(input())
l = list(map(int, input().split()))
x = int(input())

a = [0 for _ in range(n)]
a[0] = l[0]
for i in range(1, n):
    a[i] = a[i-1] + l[i]

s = a[-1]
k = (x//s)*n
x %= s
i = 0
while a[i] <= x:
    i += 1
k += i + 1
print(k)