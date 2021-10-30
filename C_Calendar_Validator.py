n, m = map(int, input().split())
b = []
for i in range(n):
    b.append(list(map(int, input().split())))

ok = True
x = b[0][0]
if x%7 + m - 1 > 7 or (x%7 == 0 and m > 1):
    ok = False
else:
    for i in range(n):
        for j in range(m):
            if x != b[i][j]:
                ok = False
                break
            x += 1
        x -= m
        x += 7
        if not ok:
            break
print('Yes' if ok else 'No')