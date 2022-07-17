n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
la = []
for i in range(n):
    la.append( (-a[i], i) )
la.sort()
ans = []
for i in range(x):
    ans.append(la[i][1])

lb = []
for i in range(x, n):
    j = la[i][1]
    lb.append( (-b[j], j) )
lb.sort()
for i in range(y):
    ans.append(lb[i][1])

lc = []
for i in range(y, n-x):
    j = lb[i][1]
    lc.append ( (-a[j] - b[j], j) )
lc.sort()
for i in range(z):
    ans.append(lc[i][1])

ans.sort()

for c in ans:
    print(c+1)