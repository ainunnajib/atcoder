from collections import defaultdict
d = defaultdict(int)
for c in input():
    d[c] += 1
done = False
for c in d:
    if d[c] == 1:
        print(c)
        done = True
        break
if not done:
    print(-1)