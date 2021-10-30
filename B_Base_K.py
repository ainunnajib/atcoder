k = int(input())
a, b = input().split()
x = 0
i = 0
for c in a[::-1]:
    x += int(c) * (k**i)
    i += 1
y = 0
i = 0
for c in b[::-1]:
    y += int(c) * (k**i)
    i += 1
print(x*y)