a = input()
enc = {}
dec = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    enc[alphabet[i]] = a[i]
    dec[a[i]] = alphabet[i]
n = int(input())
l = []
rev = {}
for _ in range(n):
    s = input()
    t = ''
    for c in s:
        t += dec[c]
    l.append(t)
    rev[t] = s
l.sort()
for x in l:
    print(rev[x])