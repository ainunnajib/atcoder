import heapq, bisect
from collections import defaultdict
n, k = map(int, input().split())
p = list(map(int, input().split()))

l = []
dl = defaultdict(list)
dc = defaultdict(int)
g = {}
stack = 0
b = []
ans = [-1 for _ in range(n)]
step = 0
for x in p:
    step += 1
    # find in sorted b, the smallest but >= x
    lenb = len(b)
    i = bisect.bisect(b, x)
    # replace it with x, doesn't change sorting order
    if i < lenb:
        gx = g[b[i]]
        g[x] = gx
        b[i] = x
        # append x to list l referenced by this group
        dl[gx].append(x)
        # increase count, if hits k, remove it from b, 
        dc[gx] += 1
        if dc[gx] == k:
        # update ans for all in that l, remove from l too
            for y in dl[gx]:
                ans[y-1] = step
            del b[i]
    # if cannot find, it's appended at the end, as it's largest
    else:
        b.append(x)
        stack += 1
        g[x] = stack
    # build the l for this new group
        dl[stack].append(x)
        dc[stack] += 1
        if dc[stack] == k:
        # update ans for all in that l, remove from l too
            for y in dl[stack]:
                ans[y-1] = step
            del b[i]
for x in ans:
    print(x)
