def isConf(a, b, c, d):
	x = a*10 + c
	y = b*10 + d
	return x >= 0 and x <= 23 and y >= 0 and y <= 59

h, m = map(int, input().split())
a = h//10
b = h%10
c = m//10
d = m%10

while(not isConf(a, b, c, d)):
	d += 1
	if d > 9:
		d = 0
		c += 1
	if c > 5:
		c = 0
		b += 1
	if b > 9:
		b = 0
		a += 1
	if a > 1 and b > 3:
		a = 0
		b = 0
print(a*10 + b, c*10 + d)