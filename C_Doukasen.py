n = int(input())
l = []
s = 0.0
for _ in range(n):
    a, b = map(float, input().split())
    s += a/b
    l.append((a, b))
s /= 2
d = 0.0
i = 0
while s >= l[i][0]/l[i][1]:
    s -= l[i][0]/l[i][1]
    d += l[i][0]
    i += 1
d += s*l[i][1]
print(d)