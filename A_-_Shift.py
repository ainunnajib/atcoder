n, k = map(int, input().split())
l = list(map(int, input().split()))
a = [0] * n
if k < n:
	for i in range(n-k):
		a[i] = l[i+k]
print(*a)