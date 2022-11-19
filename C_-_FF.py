from collections import defaultdict
a = defaultdict(bool)

n, q = map(int, input().split())
for _ in range(q):
	t, x, y = map(int, input().split())
	x -= 1
	y -= 1
	if t == 1:
		a[(x,y)] = True
	elif t == 2:
		a[(x,y)] = False
	else:
		print('Yes' if a[(x,y)] and a[(y,x)] else 'No')