from collections import defaultdict
n = int(input())
d = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    d[a] += 1
    d[a+b] -= 1

days = 0
k = [0 for i in range(n+1)]
prev = 0
p = 0
for x in sorted(d.keys()):
    k[p] += x-prev
    p += d[x]
    prev = x
s = [str(c) for c in k]
print(' '.join(s[1:]))