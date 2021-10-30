n, q = map(int, input().split())
front = [-1 for i in range(n)]
back = [-1 for i in range(n)]
for _ in range(q):
    l = input()
    if l[0] == '3':
        c, x = map(int, l.split())
        x -= 1
        while front[x] != -1:
            x = front[x]
        s = []
        while x != -1:
            s.append(str(x+1))
            x = back[x]
        print(len(s), ' '.join(s))
    else:
        c, x, y = map(int, l.split())
        x -= 1
        y -= 1
        if c == 1:
            front[y] = x
            back[x] = y
        else:
            front[y] = -1
            back[x] = -1