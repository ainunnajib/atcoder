h, w = map(int, input().split())
l = []
for r in range(h):
    l.append(list(map(int, input().split())))
ok = True
for r in range(h):
    for c in range(w):
        for i in range(r+1, h):
            for j in range(c+1, w):
                if l[r][c] + l[i][j] > l[i][c] + l[r][j]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            break
    if not ok:
        break
print('Yes' if ok else 'No')