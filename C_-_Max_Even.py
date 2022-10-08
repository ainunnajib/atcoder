n = int(input())
a = list(map(int, input().split()))
o = []
e = []
for x in a:
  if x%2 == 0:
    e.append(x)
  else:
    o.append(x)
o.sort(reverse=True)
e.sort(reverse=True)
if len(e) <= 1 and len(o) <= 1:
  print(-1)
elif len(e) <= 1:
  print(o[0]+o[1])
elif len(o) <= 1:
  print(e[0]+e[1])
else:
  print(max(o[0]+o[1], e[0]+e[1]))