def dist(p, q):
    return (p[0]-q[0])**2 + (p[1]-q[1])**2

g = []
for i in range(9):
    g.append([c == '#' for c in input()])
o = []
for i in range(9):
    for j in range(9):
        if g[i][j]:
            o.append((i, j))

ans = 0
for i in range(len(o)):
    for j in range(i+1, len(o)):
        for k in range(j+1, len(o)):
            for l in range(k+1, len(o)):
                a = dist(o[i], o[j])
                b = dist(o[j], o[k])
                c = dist(o[k], o[l])
                d = dist(o[l], o[i])
                e = dist(o[i], o[k])
                f = dist(o[j], o[l])
                if a == b and b == c and c == d and e == f:
                    ans += 1
                    continue
                a = dist(o[i], o[j])
                b = dist(o[j], o[l])
                c = dist(o[l], o[k])
                d = dist(o[k], o[i])
                e = dist(o[i], o[l])
                f = dist(o[j], o[k])
                if a == b and b == c and c == d and e == f:
                    ans += 1
                    continue
                a = dist(o[i], o[k])
                b = dist(o[k], o[j])
                c = dist(o[j], o[l])
                d = dist(o[l], o[i])
                e = dist(o[i], o[j])
                f = dist(o[k], o[l])
                if a == b and b == c and c == d and e == f:
                    ans += 1
                    continue

print(ans)