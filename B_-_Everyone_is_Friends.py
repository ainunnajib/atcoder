n, m = map(int, input().split())
b = [[False for j in range(n)] for i in range(n)]
for i in range(n):
  b[i][i] = True
for _ in range(m):
  l = list(map(int, input().split()))
  for i in range(1, l[0]):
    for j in range(i+1, l[0]+1):
      x = l[i]-1
      y = l[j]-1
      b[x][y] = True
      b[y][x] = True
if sum([sum(b[i]) for i in range(n)]) == n*n:
  print('Yes')
else:
  print('No')