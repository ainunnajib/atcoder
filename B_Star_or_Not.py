from collections import defaultdict
d = defaultdict(int)
n = int(input())
star = False
for _ in range(n-1):
    a, b = map(int, input().split())
    d[a] += 1
    d[b] += 1
    if d[a] == n-1 or d[b] == n-1:
        star = True
print('Yes' if star else 'No')