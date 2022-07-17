# 1 red @n --> 1 red @n-1 + x blue @n
# 1 blue @n --> 1 red @n-1 + y blue @n-1

# 1 red @n --> x+1 red @n-1 + xy blue @n-1

n, x, y = map(int, input().split())
r, b = 1, 0
for _ in range(n-1):
    nr = b
    nb = b * y
    nb += r * x * y
    nr += r * (x+1)
    b, r = nb, nr
print(b)