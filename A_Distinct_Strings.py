from collections import defaultdict
d = defaultdict(int)
s = input()
for c in s:
    d[c] += 1
ans = 3*2*1
for c in d:
    for i in range(2, d[c]+1):
        ans //= i
print(ans)