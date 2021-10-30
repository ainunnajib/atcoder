l = list(input())
l.sort(reverse=True)
f = 0
a, b = 0, 0
n = len(l)
for i in range(n//2):
    x, y = int(l[2*i]), int(l[2*i+1])
    if (a*10+x)*(b*10+y) >= (b*10+x)*(a*10+y):
        a *= 10
        a += x
        b *= 10
        b += y
    else:
        a *= 10
        a += y
        b *= 10
        b += x
if n%2 == 0:
    print(a*b)
else:
    x = int(l[-1])
    print(max((a*10+x)*b, (b*10+x)*a))