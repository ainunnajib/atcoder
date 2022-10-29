d = {0:1}
def f(x):
    if x in d:
        return d[x]
    a = f(x//2)
    d[x//2] = a
    b = f(x//3)
    d[x//3] = b
    d[x] = a + b
    return d[x]

n = int(input())
print(f(n))