squares = set()
root = {}
for i in range(1001):
	squares.add(i*i)
	root[i*i] = i

n, m = map(int, input().split())
d = []
for i in sorted(squares):
	if i+i > m:
		break
	if m-i in squares:
		a = root[i]
		b = root[m-i]
		d.append((a, b))
		d.append((a, -b))
		d.append((-a, b))
		d.append((-a, -b))
		if a != b:
			d.append((b, a))
			d.append((b, -a))
			d.append((-b, a))
			d.append((-b, -a))

g = [[-1 for j in range(n)] for i in range(n)]
g[0][0] = 0
q = [(0, 0, 0)]
cur = 0

while cur < len(q):
	moves = q[cur][2] + 1
	for dx, dy in d:
		x = q[cur][0] + dx
		y = q[cur][1] + dy
		if x >= 0 and x < n and y >= 0 and y < n:
			if g[x][y] < 0:
				g[x][y] = moves
				q.append((x, y, moves))
	cur += 1

for l in g:
	print(*l)