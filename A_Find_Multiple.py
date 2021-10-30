ans = -1
a, b, c = map(int, input().split())
while a%c != 0 and a < b:
    a += 1
if a%c == 0:
    ans = a
print(ans)